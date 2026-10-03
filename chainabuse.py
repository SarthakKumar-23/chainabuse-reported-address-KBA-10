import os
import csv
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("CHAINABUSE_API_KEY")

url = "https://api.chainabuse.com/v0/reports"

# Test only ONE address to preserve API calls
with open("data/addresses.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    address = next(reader)["address"].strip()

params = {
    "address": address,
    "chain": "ETH",
    "page": 1,
    "perPage": 50,
}

try:
    response = requests.get(
        url,
        params=params,
        auth=(API_KEY, API_KEY),
        timeout=30,
    )

    print("Address:", address)
    print("HTTP Status:", response.status_code)
    print("Response:")

    print(response.json())

except requests.exceptions.Timeout:
    print("Request timed out.")

except requests.exceptions.RequestException as error:
    print("Network error:", error)