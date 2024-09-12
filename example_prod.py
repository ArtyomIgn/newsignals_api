import requests
import time
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)

url = 'https://oh.sssh.it/news/signals'

def check_new_news(latest_news, news_data):
    new_news = []
    latest = latest_news
    for news in news_data:
        if news['published_primary_source'] > latest_news['published_primary_source']:
            new_news.append(news)
            if news['published_primary_source'] > latest['published_primary_source']:
                latest = news
        elif news['published_primary_source'] == latest_news['published_primary_source'] and news != latest_news:
            new_news.append(news)
    return new_news, latest


latest_news = {'published_primary_source': '1970-01-01T00:00:00.000Z'}

session = requests.Session()

session.headers.update({
    'User-Agent': 'news-checker/1.0',
    'Accept': 'application/json'
})

while True:
    try:
        response = session.get(url, timeout=5)
        
        if response.status_code == 200:
            data = response.json().get('message', [])
            if data:
                new_news_list, latest_news = check_new_news(latest_news, data)
                if new_news_list:
                    for news in new_news_list:
                        logging.info(f"New news found: {news}")
        else:
            logging.error(f"Error {response.status_code}: {response.text}")
    except requests.exceptions.Timeout:
        logging.error("Request timed out.")
    except requests.exceptions.ConnectionError as e:
        logging.error(f"Connection error: {e}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

    time.sleep(1)

session.close()