import requests

url = "http://127.0.0.1:5889/log"

response = requests.post(url)

print(response.text)
