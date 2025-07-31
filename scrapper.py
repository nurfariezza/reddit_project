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
   

def fetch_data():
    response = requests.get("https://www.reddit.com/r/malaysia/hot.json?limit=10", headers=config.REDDIT_HEADER)

    data = response.json()
    for post in data['data']['children']:
        print(post['data']['title'], post['data']['url'])


reddit = login()
if reddit:
    print("Welcome User:",reddit.user.me())
    fetch_data()

