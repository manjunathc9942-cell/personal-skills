import requests
head = {
    "Accept" : "text/plain"
}
response = requests.get('https://fakerestapi.azurewebsites.net/api/v1/Activities', headers=head)
print(response.json())
print(response.status_code)
assert response.status_code == 200