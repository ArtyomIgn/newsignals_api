import requests

url = "https://oh.sssh.it/news/free-signals"

headers = {
    "token": "..." # insert your token here
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("Response JSON:", response.json())
else:
    print("Request failed with status code:", response.status_code)