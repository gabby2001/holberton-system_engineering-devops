#!/usr/bin/python3
'''Use Reddit API to query data'''
import requests


def recurse(subreddit, hot_list=[], after=None):
    '''Use recursion to return a list of hot articles of a subreddit'''
    header = {'User-agent': 'Chrome/66.0.3359.139 Safari/537.36'}
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'\
          .format(subreddit, after)
    r = requests.get(url, headers=header)

    if r.status_code == 200:
        for item in r.json().get('data').get('children'):
            hot_list.append(item.get('data').get('title'))
        after = (r.json().get('data').get('after'))
        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
    else:
        return None
