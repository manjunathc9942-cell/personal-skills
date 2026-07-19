
import requests

head = {
"accept": "text/plain",
"Content-Type": "application/json"
}

request_payload = {
    "id": 25,
    "idBook": "232322",
    "firstName": "Ganandeep",
    "lastName": "C",
    "phone_number": 947828443
}

response = requests.post("https://fakerestapi.azurewebsites.net/api/v1/Authors",
                         json=request_payload,
                         headers=head)
print(response.json())
print(response.status_code)
data = response.json()
assert response.status_code == 200
assert data["id"] == 25
assert str(data["idBook"]) == "232322"
assert data["firstName"] == "Ganandeep"
assert data["lastName"] == "C"