from .fetcher import fetch_posts
from .schemas import Post
import threading
from functools import partial

def update_by_timeout():

    Post.drop_collection()

    posts = fetch_posts()

    for post in posts:
        Post(text=post["text"], photos=post["photos"]).save()
    print(threading.active_count())
    print('update_done  ')
    threading.Timer(30*60, update_by_timeout).start()
    threading.Event().set()
    


