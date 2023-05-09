#!/usr/bin/python3
"""
Recursive function that queries the Reddit API, parses the title of all hot
articles, and prints a sorted count of given keywords
"""

import requests


def count_words(subreddit, word_list, after='', word_dict={}):
    """
    Queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords.

    subreddit (str): The subreddit to search.
    word_list (list): List of keywords to search for.
    after (str): Parameter for pagination.
    word_dict (dict): Dictionary containing the counts for each keyword.

    Returns:
        None.
    """

    # Set the User-Agent header to avoid the Too Many Requests error.
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
               AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110\
               Safari/537.36'}

    # Create the URL and request the data from the Reddit API.
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
        subreddit, after)
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the subreddit is invalid.
    if response.status_code != 200:
        return None

    # Get the data from the response.
    data = response.json().get('data')
    children = data.get('children')
    after = data.get('after')

    # Loop through each post and parse the title.
    for child in children:
        title = child.get('data').get('title').lower()

        # Loop through the word list and check if it is in the title.
        for word in word_list:
            count = title.count(word.lower())

            # Add the count to the word dictionary.
            if count > 0:
                if word.lower() in word_dict:
                    word_dict[word.lower()] += count
                else:
                    word_dict[word.lower()] = count

    # Recursively call the function if there are more pages to parse.
    if after is not None:
        count_words(subreddit, word_list, after, word_dict)
    else:
        # Sort by count (descending) and then alphabetically (ascending).
        sorted_words = sorted(word_dict.items(), key=lambda x: (-x[1], x[0]))

        # Print the sorted words.
        for word, count in sorted_words:
            print('{}: {}'.format(word, count))
