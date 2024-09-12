import requests

url = 'https://oh.sssh.it/news/signals'

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")