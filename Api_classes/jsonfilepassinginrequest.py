import warnings
import urllib3

# Keeps your terminal output clean from the NotOpenSSLWarning
warnings.filterwarnings("ignore", category=urllib3.exceptions.NotOpenSSLWarning)

import requests
import json

base_url = 'https://reqres.in/api/users'

# FIXED: Removed the stray underscore and space from the key
headers_test = {'Content-Type': 'application/json'}

# Best practice: opens and automatically closes the file for you
with open('./userdata.json', 'r') as json_file:
    json_payload = json.load(json_file)

# FIXED: Changed 'json=payload' to use 'json=json_payload'
response = requests.post(url=base_url, headers=headers_test, json=json_payload)

print(response.status_code)
print(response.text)