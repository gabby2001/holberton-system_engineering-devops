#!/usr/bin/python3
'''Gather data from API'''
import requests
from sys import argv


def todo(id):
    '''Get numbers of task done and task list'''
    # get user name by id
    r = requests.get('https://jsonplaceholder.typicode.com/users')
    for user in r.json():
        if int(id) == user.get('id'):
            name = user.get('name')

    # get data of todo items
    r = requests.get('https://jsonplaceholder.typicode.com/todos')
    total = 0
    done = 0
    tasks = []
    for item in r.json():
        if int(id) == item.get('userId'):
            total += 1
            if item.get('completed') == True:
                done += 1
                tasks.append(item.get('title'))

    # print result
    print('Employee {} is done with tasks({}/{}):'.format(name, done, total))
    for task in tasks:
        print('\t ' + task)


if __name__ == '__main__':
   todo(argv[1])
