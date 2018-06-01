import praw
import config
import time


def bot_login():
    r = praw.Reddit(client_id=config.client_id,
                    client_secret=config.client_secret,
                    user_agent=config.user_agent,
                    username=config.username,
                    password=config.password)
    return r


def bot_run(r):
    for comment in r.subreddit('test').comments(limit=25):
        if "dog" in comment.body:
            print("Post with \"dog\" found! And it's id is " + comment.id)
            comment.reply("Atleast now it is working")
            print("Replied to comment " + comment.id)

    time.sleep(10)


r = bot_login()
bot_run(r)
