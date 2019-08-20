
from .fetcher import fetch_posts
from .schemas import Post, Photo
from flask import current_app
import threading
from functools import partial

def update_by_timeout(timeout=30*60):
    Post.drop_collection()

    posts = fetch_posts()

    for post in posts:
        db_photos = [Photo(url=url) for url in post["photos"]]
        Post(text=post["text"], photos=db_photos).save()
    print('update_done  ')
    threading.Timer(timeout, partial(update_by_timeout, timeout)).start()

# update_by_timeout()
