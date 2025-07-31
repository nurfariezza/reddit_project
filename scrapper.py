import json
import praw, requests, config
from datetime import datetime

def login():
    try:
        reddit = praw.Reddit(
            client_id=config.CLIENT_ID,
            client_secret=config.SECRET_KEY,
            username=config.USERNAME,
            password=config.PASSWORD,
            user_agent=config.USER_AGENT
        )

        user = reddit.user.me()
        if user:
            return reddit         
    except Exception as e:
        print("Login failed:", e)

def fetch_data(pages, limit):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M")
    filename = f"reddit_content_{timestamp}.json"
    after = None
    base_url = "https://www.reddit.com/r/malaysia/hot.json"
    result = []    
    idx = 1 

    for _ in range(pages):
        params = { "limit": limit,
                "after": after
        }
        response = requests.get(base_url, headers=config.REDDIT_HEADER, params = params)
        mainData = response.json()
        print(pages, limit)

        children = mainData['data']['children']
        after = mainData['data']['after']
        for content in children:
            subContentData = {
                "id":idx,
                "post_title":content['data']['title'],
                "image_url":content['data']['url'],
                "post_created_date":content['data']['created'],
            }
            result.append(subContentData)
            idx += 1

    with open(filename, 'w') as file:
        json.dump(result,file, indent=4)
        print(f"Saved {len(result)} posts to {filename}")

reddit = login()
if reddit:
    print("Welcome User:",reddit.user.me())
    fetch_data(pages = 10, limit = 10)

