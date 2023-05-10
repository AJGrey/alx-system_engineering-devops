#!/usr/bin/python3
""" A function that queries the Reddit API and returns the number of subscriber
"""

import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/" + subreddit + "/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    data = response.json()['data']
    subscribers = data['subscribers']
    return subscribers
