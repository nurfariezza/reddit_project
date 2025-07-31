import json
import os
from urllib import response
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
   

def fetch_data():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M")
    filename = f"reddit_content_{timestamp}.json"

    response = requests.get("https://www.reddit.com/r/malaysia/hot.json?limit=50", headers=config.REDDIT_HEADER)
    mainData = response.json()

    result = []     
    for idx, content in enumerate(mainData['data']['children'],start=1):
        subContentData = {
            "id":idx,
            "content_title":content['data']['title'],
            "content_image_url":content['data']['url'],
            "content_created_date":content['data']['created'],
        }
        result.append(subContentData)
    with open(filename, 'w') as file:
        json.dump(result,file, indent=4)

reddit = login()
if reddit:
    print("Welcome User:",reddit.user.me())
    fetch_data()

