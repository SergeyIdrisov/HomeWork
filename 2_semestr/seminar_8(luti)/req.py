import requests
response = requests.request("POST", 'http://127.0.0.1:5000/login', data={'username': 'Klimkou', 'password': '1234'})

print(response.text)
