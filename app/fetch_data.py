import requests
import json
import time
import csv

pools_list = []

# Fetch POOL ADDRESSES
for i in range(1, 11):
    pools_url = "https://api.geckoterminal.com/api/v2/networks/ton/pools"
    base_params = {
        "network": "ton",
        "page": i,
    }

    response = requests.get(pools_url, params=base_params)
    results = response.json()

    if "data" in results and len(results["data"]) > 0:
        keys_to_print = ["name", "address"]

        for pool in results["data"]:
            lim_pool_inf = {key: pool["attributes"][key] for key in keys_to_print}
            pools_list.append(lim_pool_inf["address"])

            print(lim_pool_inf)
    else:
        print("No pools found.")
    print(f"Page {i}")

print("Pool addresses:", pools_list)


# with open("pool_list.csv", mode="w", newline='') as file:
#     writer = csv.writer(file)
#     for pool in pools_list:
#         writer.writerow([pool])






# time.sleep(60)

# base_params_ohlcv = {
#     "network": "ton",
#     "timeframe": "day",
#     "aggregate": 1,
#     "limit": 1,
#     "currency": "usd",
# }

params = { 
    "aggregate": 1,
    "limit": 10,
}

for pool_address in pools_list:
    ohlcv_url = f"https://api.geckoterminal.com/api/v2/networks/ton/pools/{pool_address}/ohlcv/day"
    
    params["pool_address"] = pool_address

    response = requests.get(ohlcv_url, params=params)
    
    if response.status_code == 429:
        time.sleep(60)
        response = requests.get(ohlcv_url, params=params)

    # if response.status_code == 200:
    results = response.json()
    print(results)
    #     if "data" in results and len(results["data"]) > 0:
    #         for pool in results["data"]:
    #             # Define the keys you want to print
    #             keys_to_print = ["open", "close"]  # Replace with actual keys
    #             limited_pool_info = {key: pool["attributes"].get(key) for key in keys_to_print}
    #             print(f"Pool Address: {pool_address}")
    #             print(json.dumps(limited_pool_info, indent=4))
    #     else:
    #         print(f"No OHLCV data found for pool address: {pool_address}")
    # else:
    #     print(f"Failed to fetch data for pool address: {pool_address} with status code {response.status_code}")
