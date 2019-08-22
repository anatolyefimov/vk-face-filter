import requests
import json
from .image_checker import check
import os

class VkApiError(Exception):
  pass


def fetch_posts():

    with open('./src/following.json') as f:
        following = json.load(f)
    
    result = []
    
    for contact in following:
        params = contact
        params["count"] = 20
        params["access_token"] = "e9d5075ca98092d49302d8b252177d7293a8482dc3259172cc4cb0d25aa8d8514dd447cad5745cd1deab2",
        params["v"] = "5.101"
        res = requests.get('https://api.vk.com/method/wall.get', params=params).json()
        if "error" in res:
            raise VkApiError(res["error"]["error_msg"])
        
        res = res["response"]
        size = res["count"]

        for post in res["items"]:
            is_good_post = False
            photo_urls = []
            text = post["text"]
            if "attachments" in post:
                attachments = post["attachments"]
            else:
                attachments = {}
            try:
                for attachment in attachments:
                    if attachment["type"] == 'photo':
                        photo_url = attachment["photo"]["sizes"][-1]["url"]
                        photo_urls.append(photo_url)

                        flag = check(photo_url)
                        is_good_post = is_good_post or flag
            except KeyError:
                print("----KeyError----")
                print(post)
            if is_good_post:
                result.append(
                    {
                        "text": text,
                        "photos": photo_urls
                    }
                )
            
    return result
