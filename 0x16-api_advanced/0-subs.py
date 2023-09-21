#!/usr/bin/python3
""" Querying Reddit API"""


import requests

def number_of_subscribers(subreddit):
    """get the no of subcribers from a subreddit recursively"""
    headers = {'User-Agent': 'Chrome-X',
              'Content-Type': 'application/json, charset=UTF-8'}
    url = 'https://reddit.com/r/{}/about.json'.format(subreddit)

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        else:
            return 0
    except requests.exceptions.RequestException:
        return 0
    