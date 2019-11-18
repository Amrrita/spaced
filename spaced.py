from __future__ import print_function, unicode_literals
from pprint import pprint
from PyInquirer import style_from_dict, Token, prompt, Separator
from examples import custom_style_2
import json


with open('data_file.json') as f:
    data = json.load(f)

    # Control flow to handle empty lists
    if len(data["daily"]) != 0:
        daily = data["daily"]
    else:
        daily = ["There are no tasks in this list"]

    if len(data["second"]) != 0:
        second = data["second"]
    else:
        second = ["There are no tasks in this list"]

    if len(data["weekly"]) != 0:
        weekly = data["weekly"]
    else:
        weekly = ["There are no tasks in this list"]

    # Py Inquirer Questions
    main_menu = [
        {
            'type': 'list',
            'name': 'which_task',
            'message': 'What do you want to do?',
            'choices': [
                'View Tasks',
                'Add Task',
                'Push Task Up',
            ]
        },
    ]

    view_tasks = [
        {
            'type': 'list',
            'name': 'view_task',
            'message': 'Which list would you like to view?',
            'choices': [
                'Daily',
                'Every Other Day',
                'Weekly',
            ]
        },
    ]

    view_tasks_add = [
        {
            'type': 'list',
            'name': 'view_task_add',
            'message': 'Which list would you like to add the task to?',
            'choices': [
                'Daily',
                'Every Other Day',
                'Weekly',
            ]
        },
    ]

    show_tasks_daily = [
        {
            'type': 'list',
            'name': 'view_task_daily',
            'message': 'Here are your Daily Tasks:',
            'choices': daily
        },
    ]

    show_tasks_second = [
        {
            'type': 'list',
            'name': 'view_task_second',
            'message': 'Here are your Every Other Day Tasks:',
            'choices': second
        },
    ]

    show_tasks_weekly = [
        {
            'type': 'list',
            'name': 'view_task',
            'message': 'Here are your Weekly Tasks:',
            'choices': weekly
        },
    ]

    def print_tasks(list_name):
        for key in data:
            if key == list_name:
                if len(data[list_name]) != 0:
                    for item in data[list_name]:
                        print(item)
                else:
                    print("There are no tasks in this list")

    # Write task to json
    def add_task_json(list_name):
        print("Enter task name: ")
        task_name = input()
        data[list_name].append(task_name)
        with open('data_file.json', "w") as write_file:
            json.dump(data, write_file)
        print(task_name + " has been added to " + list_name + "!")


def main():

    while True:
        main_menu_selection = prompt(main_menu, style=custom_style_2)

        # View Task Control Flow
        if main_menu_selection['which_task'] == 'View Tasks':
            view_tasks_selection = prompt(view_tasks, style=custom_style_2)

            if (view_tasks_selection['view_task']).lower() == 'daily':
                print_tasks("daily")

            elif (view_tasks_selection['view_task']).lower() == 'every other day':
                print_tasks("second")

            else:
                print_tasks("weekly")

        # Add Task Control Flow
        elif main_menu_selection['which_task'] == 'Add Task':
            view_tasks_selection = prompt(view_tasks_add, style=custom_style_2)

            if (view_tasks_selection['view_task_add']).lower() == 'daily':
                add_task_json("daily")

            elif (view_tasks_selection['view_task_add']).lower() == 'every other day':
                add_task_json("second")

            elif (view_tasks_selection['view_task_add']).lower() == 'weekly':
                add_task_json("weekly")

        else:
            break


if __name__ == "__main__":
    main()


# pprint(answers)
