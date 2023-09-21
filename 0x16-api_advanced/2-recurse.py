#!/usr/bin/python3

""" Querying Reddit API Recursively"""

import requests


def recurse(subreddit, hot_list=[]):
    """get the no of subscribers recursively"""

    headers = {'User-Agent': 'Chrome-X',
               'Content-Type': 'application/json, charset=UTF-8'}
    url = 'https://reddit.com/r/{}/hot.json'.format(subreddit)

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']

            for post in posts:
                title = post['data']['title']
                hot_list.append(title)

            # Check if there's another page to fetch
            after = data['data']['after']
            if after is not None:
                return recurse(subreddit, hot_list)
            else:
                return hot_list
        else:
            return None
    except requests.exceptions.RequestException:
        return None
