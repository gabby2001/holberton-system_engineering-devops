#!/usr/bin/python3
'''Use Reddit API ot query data'''
import requests


def number_of_subscribers(subreddit):
    '''Query number of subscribers of a subreddit'''
    user_agent = {'User-agent': 'Chrome/66.0.3359.139 Safari/537.36'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    r = requests.get(url)
    if r.status_code == 200:
        print(r.json().get('data').get('subscribers'))
    else:
        return 0
