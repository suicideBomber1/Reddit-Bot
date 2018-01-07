import praw


def bot_login():
    r = praw.Reddit(client_id='X3Ie9jxGC6Ww0w',
                    client_secret='B_hCvDGwrJBtxCfrp9_J7nnOgEg',
                    user_agent='praw_tut',
                    username='Bot_G',
                    password='SAIRAM369')
    return r
