import warnings
import urllib3
import requests

# Keep the terminal clean from the SSL warning
warnings.filterwarnings("ignore", category=urllib3.exceptions.NotOpenSSLWarning)

head = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ec1a5713623d266455e18b8bf52ed0a58c...' # Add your full token here
}

body = {
    "name": "Prasanth 123",
    # TIP: Remember to change this email slightly each run since GoRest requires unique emails!
    "email": "test12398y234682364@gmail.com",
    "gender": "male",
    "status": "active"
}

url = 'https://gorest.co.in/public/v2/users'

# 1. Create the user (POST)
respone = requests.post(url, headers=head, json=body)
print("POST Response:")
print(respone.json())

assert respone.status_code == 201

# 2. Extract the ID safely and fetch the user (GET)
# Using an f-string automatically converts the integer ID into a string for the URL path
user_id = respone.json()['id']
get_url = f"{url}/{user_id}"

getResponse = requests.get(get_url, headers=head)
print("\nGET Response:")
print(getResponse.json())

assert getResponse.status_code == 200