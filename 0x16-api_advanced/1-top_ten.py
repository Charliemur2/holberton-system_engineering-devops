#!/usr/bin/python3

"""
Write a function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""


import requests


def top_ten(subreddit):
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    req = requests.get(url, headers={'User-agent': 'Carlos'},
                       allow_redirects=False, params={'limit': 10})
    if req.json().get('data'):
        for posts in req.json().get('data').get('children'):
            print(posts.get('data').get('title'))
    else:
        print('None')
