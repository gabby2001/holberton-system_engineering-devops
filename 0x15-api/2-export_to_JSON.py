#!/usr/bin/python3
'''Gather data from API and expoer as json'''
import json
import requests
from sys import argv


def to_json(id):
    '''Get numbers of task done and task list and export as json file'''
    # get username by id
    r = requests.get('https://jsonplaceholder.typicode.com/users')
    for user in r.json():
        if int(id) == user.get('id'):
            name = user.get('username')

    # get data of todo items
    r = requests.get('https://jsonplaceholder.typicode.com/todos')
    tasks = []
    for item in r.json():
        if int(id) == item.get('userId'):
            tasks.append({'task': item.get('title'),
                          'completed': item.get('completed'),
                          'username': name})

    # write to json file
    filename = id + '.json'
    data = {int(id): tasks}
    with open(filename, 'w') as f:
        f.seek(0)
        json.dump(data, f, ensure_ascii=False)


if __name__ == '__main__':
    to_json(argv[1])
