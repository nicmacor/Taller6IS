class Task:
    def __init__(self, name, description, status='Incomplete'):
        self.name = name
        self.description = description
        self.status = status


class ToDoList:
    def __init__(self):
        self.tasks = []
    
    #add_tasks
    def add_task(self, name, description):
        task = Task(name, description)
        self.tasks.append(task)
        print(f"Task '{name}' added to the to-do list.")


    #List tasks
    def list_tasks(self):
        if not self.tasks:
            print('No tasks found.')
        else:
            print('To-Do List:')
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task.name} - {task.description}")
        return self.tasks

    #List incomplete Tasks NEW FEATURE
    def list_incomplete_tasks(self):
        taskI=[]
        if not self.tasks:
            print('No tasks found.')
        else:
            print('To-Do List (incompleted):')
            for index, task in enumerate(self.tasks, start=1):
                if task.status == 'Incomplete':
                    print(f"{index}. {task.name} - {task.status}")
                    taskI.append(task)
        return taskI

    #Mark task ass completed
    def mark_complete(self,task_index):
        if task_index>0 and task_index <= len(self.tasks):
            task=self.tasks[task_index-1]
            task.status='Completed'
            print(f'Task "{task.name}" marked as complete.')
        else:
            print('Invalid task index.')


    def get_task(self,nombre):
        for index, task in enumerate(self.tasks, start=1):
                if task.name.lower() == nombre.lower():
                    return task



    #Edit task NEW FEATURE
    def edit_task(self,task_index, new_name, new_description):
        if 1 <= task_index <= len(self.tasks):
            task=self.tasks[task_index-1]
            task.description = new_description
            task.name=new_name
            print(f'Task edited successfully.')
        else:
            print('Invalid task index.')

    #Clear all tasks
    def clear_tasks(self):
        self.tasks=[]
        print('To-do list cleared successfully!')

def main():
    toDoList=ToDoList()
    while True:
        print('\nTo-Do List Manager\n'
              '1. Add a new task\n'
              '2. List all tasks\n'
              '3. Mark a task as completed\n'
              '4. Clear the entire to-do list\n'
              '5. List all incomplete tasks\n'
              '6. Edit a task\n'
              '7. Quit')

        choice = input('Enter your choice (1-7): ')

        if choice == '1':
            name = input('Enter task name: ')
            description = input('Enter task description: ')
            toDoList.add_task(name, description)
        elif choice == '2':
            toDoList.list_tasks()
        elif choice == '3':
            toDoList.list_tasks()
            task_index = int(input('Enter the index of the task to mark as complete: '))
            toDoList.mark_complete(task_index)
        elif choice == '4':
            toDoList.clear_tasks()
        elif choice == '5':
            toDoList.list_incomplete_tasks()
        elif choice == '6':
            toDoList.list_tasks()
            task_index = int(input('Enter the index of the task to edit: '))
            new_name = input('Enter the new task name: ')
            new_description = input('Enter the new task description: ')
            toDoList.edit_task(task_index, new_name, new_description)
        elif choice == '7':
            print('Exiting the To-Do List Manager. Goodbye!')
            break
        else:
            print('Invalid choice. Please enter a number between 1 and 5.')

if __name__ == "__main__":
    main()