import requests
import csv

def fetch_pool_addresses():
    pools_list = []
    for i in range(1, 11):  # Adjust the range as needed
        pools_url = "https://api.geckoterminal.com/api/v2/networks/ton/pools"
        base_params = {"network": "ton", "page": i}

        response = requests.get(pools_url, params=base_params)
        results = response.json()

        if "data" in results and len(results["data"]) > 0:
            for pool in results["data"]:
                pool_address = pool["attributes"]["address"]
                pools_list.append(pool_address)
        else:
            break  # Stop if no more pools are found

    with open("pool_list.csv", mode="w", newline='') as file:
        writer = csv.writer(file)
        for pool in pools_list:
            writer.writerow([pool])

    return pools_list

pools_list = fetch_pool_addresses()
print("Fetched pool addresses:", pools_list)
