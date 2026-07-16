import warnings
import urllib3

# Hides the NotOpenSSLWarning from your terminal output
warnings.filterwarnings("ignore", category=urllib3.exceptions.NotOpenSSLWarning)

import requests

para = {
    'page': 1,
    'per_page': 3
}

url = 'https://gorest.co.in/public/v2/users'

response = requests.get(url, params=para)

print("Pagination Output (Limit 3):")
print(response.json())

assert response.status_code == 200