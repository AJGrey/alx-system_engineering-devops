#!/usr/bin/python3
"""
A function that queries the Reddit API and prints the
titles of the first 10 hot posts listed for a given
subreddit.
"""

import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/" + subreddit + "/hot.json?limit=10"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print("None")
        return

    data = response.json()['data']
    children = data['children']

    for child in children:
        title = child['data']['title']
        print(title)
