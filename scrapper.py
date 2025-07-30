from urllib import response
import praw, requests, config

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


