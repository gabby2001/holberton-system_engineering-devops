#!/usr/bin/python3
'''Use Reddit API to query data'''
import requests


def top_ten(subreddit):
    '''Print frist 10 posts of a subreddit'''
    user_agent = {'User-agent': 'Chrome/66.0.3359.139 Safari/537.36'}
    url = 'https://www.reddit.com/r/{}/new.json?limit=10'.format(subreddit)
    r = requests.get(url)
    if r.status_code == 200:
        for item in r.json().get('data').get('children'):
            print(item.get('data').get('title'))
    else:
        print('None')
