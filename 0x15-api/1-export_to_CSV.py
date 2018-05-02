#!/usr/bin/python3
'''Gather data from API and expoer as CSV'''
import csv
import requests
from sys import argv


def to_csv(id):
    '''Get numbers of task done and task list and export as json'''
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
            tasks.append({'USER_ID': int(id), 'USERNAME': name,
                          'TASK_COMPLETED_STATUS': item.get('completed'),
                          'TASK_TITLE': item.get('title')})

    # write to csvfile
    filename = id + '.csv'
    with open(filename, 'w', newline='') as csvfile:
        f = csv.writer(csvfile)
        for elem in tasks:
            f.writerow([elem['USER_ID'], elem['USERNAME'],
                        elem['TASK_COMPLETED_STATUS'], elem['TASK_TITLE']])


if __name__ == '__main__':
    to_csv(argv[1])
