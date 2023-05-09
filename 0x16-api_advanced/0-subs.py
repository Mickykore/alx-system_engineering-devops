#!/usr/bin/python3

import requests

"""Function to query subscribers on a given Reddit subreddit."""


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
            'User-Agent': 'Mozilla/5.0'
            }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        return response.json()['data']['subscribers']
    else:
        return 0
