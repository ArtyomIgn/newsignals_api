import requests

url = 'https://api.rosggram.ru/news/signals'

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")