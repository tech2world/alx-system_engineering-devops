#!/usr/bin/python3
"""Querying Reddit API"""


import requests


def top_ten(subreddit):
    """ get the first ten host post from a subbreddit"""

    headers = {'User-Agent': 'Chrome-X',
               'Content-Type': 'application/json, charset=UTF-8'}
    url = 'https://reddit.com/r/{}/hot.json'.format(subreddit)
    params = {'limit': 10}

    try:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for i, post in enumerate(posts, start=1):
                title = post['data']['title']
                print(f"{i}. {title}")

        else:
            print("None")
    except requests.exceptions.RequestException:
        return 0
