import warnings
import urllib3

# Keeps your terminal output clean from that NotOpenSSLWarning
warnings.filterwarnings("ignore", category=urllib3.exceptions.NotOpenSSLWarning)

import requests

# 1. Setup matching headers and URL targeting Authors
author_url = 'https://fakerestapi.azurewebsites.net/api/v1/Authors/15'
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

# 2. Check the data BEFORE the modification
print("--- Before request ---")
response_get = requests.get(author_url, headers=headers)
print(f"GET Status: {response_get.status_code}")
print(response_get.json())

# 3. Define the updated data layout matching the Author schema
put_payload = {
    "id": 15,
    "idBook": 101,
    "firstName": "ravi",
    "lastName": "c"
}

# 4. Perform the update and check the data AFTER
print("\n--- After request ---")
response_put = requests.put(author_url, headers=headers, json=put_payload)
print(f"PUT Status: {response_put.status_code}")
print(response_put.json())

author_url = 'https://fakerestapi.azurewebsites.net/api/v1/Authors/15'
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

# 2. Check the data BEFORE the modification
print("--- Details after put request ---")
response_get = requests.get(author_url, headers=headers)
print(f"GET Status: {response_get.status_code}")
print(response_get.json())
