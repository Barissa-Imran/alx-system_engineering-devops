#!/usr/bin/python3
""" prints the titles of the first 10 hot posts"""

import requests


def top_ten(subreddit):
    """ prints the titles of the first 10 hot posts"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 \
            Mobile Safari/537.36"
    }
    param = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=param,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(top.get("data").get("title")) for top in results
     .get("children")]
