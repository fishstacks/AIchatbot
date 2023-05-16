import requests

url = "http://localhost:5005/webhooks/rest/webhook"
data = {"message": "Hi"}
response = requests.post(url, json=data)

print(response.json())
