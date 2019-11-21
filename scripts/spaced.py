from PyInquirer import style_from_dict, Token, prompt, Separator
from examples import custom_style_1
import json
import random


with open('../json/data_file.json') as f:
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
    
    if len(data["daily"]) or len(data["second"]) or len(data["weekly"]) != 0:
        total = [data["daily"], data["second"], data["weekly"]]
        
    

    main_menu = [
        {
            'type': 'list',
            'name': 'which_task',
            'message': 'What do you want to do?',
            'choices': [
                'View Tasks',
                'Add Task',
                'Push Task Up',
                'Randomize Task',
              
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
                'All',
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

    view_tasks_random = [
        {
            'type': 'list',
            'name': 'view_task_random',
            'message': 'Which list would you like to select a random task from?',
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

    show_all_tasks = [
        {
            'type' : 'list',
            'name' : 'view_all_tasks',
            'message' :'Here are all your tasks',
            'choices' : total
        }
    ]

    # Main Loop Functions

    # Print Tasks

    def print_tasks(list_name):
        for key in data:
            if key == list_name:
                if len(data[list_name]) != 0:
                    for item in data[list_name]:
                        print(item)
                else:
                    print("There are no tasks in this list.")
    
    def print_all(total):
        print("Daily: " , total[0])
        print("Every other day: " , total[1])
        print("Weekly: " , total[2])
        for i in range(len(total)) :  
            for j in range(len(total[i])) :  
                print(total[i][j], end=" ") 
        print()  

    # Write task to json
    def add_task_json(list_name):
        print("Enter task name: ")
        task_name = input()
        data[list_name].append(task_name.lower())
        with open('../json/data_file.json', "w") as write_file:
            json.dump(data, write_file)
        print(task_name + " has been added to " + list_name + "!")

    # Push task up to next level
    def push_up(task_name):

        # Counter to check whether task does not exist in any list
        checks = 0
        for list_name in data:
            if task_name in data[list_name]:
                if list_name == "daily":
                    task_idx = data[list_name].index(task_name)
                    del data[list_name][task_idx]
                    data["second"].append(task_name)
                    with open('../json/data_file.json', "w") as write_file:
                        json.dump(data, write_file)

                    print(task_name + " has been moved up to every other day!")
                    break

                elif list_name == "second":
                    task_idx = data[list_name].index(task_name)
                    del data[list_name][task_idx]
                    data["weekly"].append(task_name)
                    with open('../json/data_file.json', "w") as write_file:
                        json.dump(data, write_file)

                    print(task_name + " has been moved up to weekly!")
                    break

                else:
                    print("The task is already at the top!")
            else:
                checks += 1
        if checks == 3:
            print("This task does not exist!")


    # Select random task
    def select_task(list_name):
        seed = random.randint(1, 100)
        selected = data[list_name][seed % len(data[list_name])]
        print("Your selected task is " + selected)

def main():

    while True:
        main_menu_selection = prompt(main_menu, style=custom_style_1)

        # View Task Control Flow
        if main_menu_selection['which_task'] == 'View Tasks':
            view_tasks_selection = prompt(view_tasks, style=custom_style_1)

            if (view_tasks_selection['view_task']).lower() == 'daily':
                print_tasks("daily")

            if (view_tasks_selection['view_task']).lower() == 'every other day':
                print_tasks("second")
            
            if (view_tasks_selection['view_task']).lower == 'weekly':
                print_tasks("weekly")

            else:
                print_all(total)

        # Add Task Control Flow
        elif main_menu_selection['which_task'] == 'Add Task':
            view_tasks_selection = prompt(view_tasks_add, style=custom_style_1)

            if (view_tasks_selection['view_task_add']).lower() == 'daily':
                add_task_json("daily")

            elif (view_tasks_selection['view_task_add']).lower() == 'every other day':
                add_task_json("second")

            elif (view_tasks_selection['view_task_add']).lower() == 'weekly':
                add_task_json("weekly")

        elif main_menu_selection['which_task'] == 'Push Task Up':
            print("Which task would you like to push up?")
            task_name = input()
            push_up(task_name)

        elif main_menu_selection['which_task'] == 'Randomize Task':
            view_tasks_selection = prompt(view_tasks_random, style=custom_style_1)

            if (view_tasks_selection['view_task_random']).lower() == 'daily':
                select_task("daily")

            elif (view_tasks_selection['view_task_random']).lower() == 'every other day':
                select_task("second")

            elif (view_tasks_selection['view_task_random']).lower() == 'weekly':
                select_task("weekly")

        else:
            break


if __name__ == "__main__":
    main()
