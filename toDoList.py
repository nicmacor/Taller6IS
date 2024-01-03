import json

def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []
    return tasks

def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)

def add_task(name, description):
    tasks = load_tasks()
    task = {'name': name, 'description': description, 'status': 'Incomplete'}
    tasks.append(task)
    save_tasks(tasks)
    print(f'Task "{name}" added successfully!')

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print('No tasks found.')
    else:
        print('To-Do List:')
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task['name']} - {task['status']}")

def mark_complete(task_index):
    tasks = load_tasks()
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1]['status'] = 'Complete'
        save_tasks(tasks)
        print(f'Task "{tasks[task_index - 1]["name"]}" marked as complete.')
    else:
        print('Invalid task index.')

def clear_tasks():
    confirmation = input('Are you sure you want to clear the entire to-do list? (yes/no): ')
    if confirmation.lower() == 'yes':
        save_tasks([])
        print('To-do list cleared successfully!')
    else:
        print('Operation canceled.')

def main():
    while True:
        print('\nTo-Do List Manager\n'
              '1. Add a new task\n'
              '2. List all tasks\n'
              '3. Mark a task as completed\n'
              '4. Clear the entire to-do list\n'
              '5. Quit')

        choice = input('Enter your choice (1-5): ')

        if choice == '1':
            name = input('Enter task name: ')
            description = input('Enter task description: ')
            add_task(name, description)
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            task_index = int(input('Enter the index of the task to mark as complete: '))
            mark_complete(task_index)
        elif choice == '4':
            clear_tasks()
        elif choice == '5':
            print('Exiting the To-Do List Manager. Goodbye!')
            break
        else:
            print('Invalid choice. Please enter a number between 1 and 5.')

if __name__ == "__main__":
    main()
