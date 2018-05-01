#!/usr/bin/python3
'''Gather data from API and expoer as json'''
import requests
import json


def all_to_json():
    '''Get task status of all employees and export as json file'''
    # get username by id
    r = requests.get('https://jsonplaceholder.typicode.com/users')
    users = {}
    for item in r.json():
        users[item.get('id')] = item.get('username')

    # get data of todo items
    r = requests.get('https://jsonplaceholder.typicode.com/todos')
    data = {}
    for id, name in users.items():
        tasks = []
        for item in r.json():
            if id == item.get('userId'):
                tasks.append({'username': name,
                             'task': item.get('title'),
                             'completed': item.get('completed')})
        data[id] = tasks

    # write to json file
    filename = 'todo_all_employees.json'
    with open(filename, 'w') as f:
        f.seek(0)
        json.dump(data, f, ensure_ascii=False)


if __name__ == '__main__':
    all_to_json()
