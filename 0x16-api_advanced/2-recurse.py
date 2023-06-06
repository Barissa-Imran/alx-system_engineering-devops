#!/usr/bin/python3
"""Returns a list containing the titles of all hot articles"""

import requests


def recurse(subreddit, hot_list=[], after=""):
    """Returns a list containing the titles of all hot articles"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 \
            Mobile Safari/537.36"
    }
    param = {
        "after": after,
        "limit": 100,
    }
    response = requests.get(url, headers=headers, params=param,
                            allow_redirects=False)
    if response.status_code == 404:
        return None
    else:
        posts = response.json().get("data").get("children")
        hot_list += [post.get("data").get("title") for post in posts]
        after = response.json().get("data").get("after")
        if after is not None:
            recurse(subreddit, hot_list, after)
        return hot_list
