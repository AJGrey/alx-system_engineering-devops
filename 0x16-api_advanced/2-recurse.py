#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and appends the
    titles of all hot articles to the hot_list.

    subreddit: string representing the subreddit to query
    hot_list: list to append article titles to
    after: identifier of the last post seen in the previous
    page of results
    """
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = 'https://www.reddit.com/r/{}/hot.json?limit=100'.format(subreddit)
    if after:
        url += '&after={}'.format(after)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return None
    data = response.json().get('data')
    if not data:
        return hot_list
    children = data.get('children')
    if not children:
        return hot_list
    for child in children:
        title = child.get('data').get('title')
        if title:
            hot_list.append(title)
    next_page = data.get('after')
    if not next_page:
        return hot_list
    return recurse(subreddit, hot_list,
                   next_page) if len(hot_list) < 1000 else hot_list[:1000]
