# Todo list

# Imports
import os
import json

def show_list(tasks):
    print()
    if not tasks:
        print('Anyone task to show')
        return

    print('Tasks:')
    for task in tasks:
        print(f'\t{task}')
    print()


def undo(tasks, undo_tasks):
    print()
    if not tasks:
        print('Anyone task to undo')
        return

    task = tasks.pop()
    print(f'{task} remove from task list')
    undo_tasks.append(task)
    print()


def remake(tasks, remake_tasks):
    print()
    if not remake_tasks:
        print('Anyone task to remake')
        return

    task = remake_tasks.pop()
    print(f'{task} added to task list')
    tasks.append(task)
    print()


def add_to_list(task, tasks):
    print()
    task = task.strip()
    if not task:
        print('You did not type a task')
        return
    print(f'{task} added to task list')
    tasks.append(task)
    print()

def read(tasks, file_path):
    datas = []
    try:
        with open(file_path, 'r', encoding='utf8') as file:
            datas = json.load(file)
    except FileNotFoundError:
        print('File not found!')
        save(tasks, file_path)
    return datas

def save(tasks, file_path):
    datas = tasks
    with open(file_path, 'w', encoding='utf8') as file:
        datas = json.dump(tasks, file, indent=2, ensure_ascii=False)
    return datas


tasks = read([], 'json_file_tasks.json')
remake_tasks = []

while True:
    print('Commands: list, undo, clear and remake')
    actions = input('Type a task: ').lower()

    commands = {
        'list': lambda: show_list(tasks),
        'undo': lambda: undo(tasks, remake_tasks),
        'remake': lambda: undo(tasks, remake_tasks),
        'clear': lambda: os.system('clear'),
        'add': lambda: add_to_list(actions, tasks),
    }

    command = commands.get(actions) if commands.get(actions) is not None else commands['add']

    command()
