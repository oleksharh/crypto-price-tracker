import requests
import time
import csv

def fetch_ohlcv_data(pools_list):
    ohlcv_data = []
    params = {"aggregate": 1, "limit": 1}

    for pool_address in pools_list:
        ohlcv_url = f"https://api.geckoterminal.com/api/v2/networks/ton/pools/{pool_address}/ohlcv/day"
        params["pool_address"] = pool_address

        response = requests.get(ohlcv_url, params=params)
        
        if response.status_code == 429:
            print("Rate limit reached. Waiting for 60 seconds...")
            time.sleep(60)
            response = requests.get(ohlcv_url, params=params)

        if response.status_code == 200:
            results = response.json()
            ohlcv_list = results['data']['attributes']['ohlcv_list']
            base_name = results['meta']['base']['name']
            base_symbol = results['meta']['base']['symbol']
            quote_name = results['meta']['quote']['name']
            quote_symbol = results['meta']['quote']['symbol']

            for ohlcv in ohlcv_list:
                ohlcv_data.append([
                    base_symbol, quote_symbol,
                    ohlcv[0], ohlcv[1], ohlcv[2], ohlcv[3], ohlcv[4],
                    ohlcv[5]
                ])

    with open("ohlcv_data.csv", mode="w", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Base Symbol", "Quote Symbol", "Timestamp", "Open", "High", "Low", "Close", "Volume"])
        writer.writerows(ohlcv_data)

    return ohlcv_data

with open("pool_list.csv", mode='r', newline='', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    pools_list = [row[0] for row in csv_reader]

ohlcv_data = fetch_ohlcv_data(pools_list)
print("Fetched OHLCV data:", ohlcv_data)
