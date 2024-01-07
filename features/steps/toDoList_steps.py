from behave import given, when, then
from toDoList import *

todo_list = ToDoList()

#1.The user wants to add a task
@given('the to do list is empty')
def step_add_task(context):
    tasks=load_tasks()

@when('User add a task with name "{name}" and description "{description}"')
def step_add_task_with_name_and_description(context, name, description):
    add_task(name, description)

@then('the task "{name}" should be added to the to-do list')
def step_task_should_be_added_to_to_do_list(context, name):
    task = get_task(name)
    assert task is not None, f"Task '{name} was not added to the to-do list"
    
##2.List the tasks in the to-do List
@given('the to-do list contains tasks')
def step_tasks_exist_in_to_do_list(context):
    add_task("Buy groceries", "Buy food and snacks")
    add_task("Pay bills", "Pay rent and ensurance")


@when('the user list all tasks')
def step_user_list_all_tasks(context):
    context.listOutput = list_tasks()

@then('the output should contain')
def step_should_see_list_of_tasks(context):
    assert context.listOutput is not None, f"No tasks were listed"

#3.The user marks a task as completed
@when('the user marks task {task_index:d} as completed')
def step_user_marks_task_completed(context, task_number):
    mark_complete(task_number)

@then('task {task_index:d} should be marked as completed')
def step_task_should_be_marked_completed(context, task_index):
    tasks=load_tasks()
    task= tasks[task_index-1]
    assert task['status'] == 'Completed', f"Task {task_index} was not marked as completed"

#4. The user wants to list the incompleted tasks
@when('the user list all incompleted tasks')
def step_user_list_all_incompleted_tasks(context):
    context.list_incomplete_output = list_incomplete_tasks()

@then('the output should contain')
def step_should_see_list_of_tasks(context):
    assert context.list_incomplete_output is not None, f"No tasks were listed"

#5.The user edits a task in the to-do list
@when('the user edits task {task_index:d} to "{new_name}" and "{new_description}"')
def step_user_edits_task(context, new_name, new_description):
    context.new_name=new_name
    context.new_description=new_description
    edit_task(task_index, new_name, new_description)

@then('the description of task {task_indec:d} should be updated')
def step_task_should_be_updated(context, task_index):
    tasks=load_tasks()
    task = tasks[task_index-1]
    assert task['description'] == context.new_description, f"Description of task '{task_index}' was not updated as expected to '{context.new_description}'"

#6. the user clears all tasks
@when('the user clears all tasks')
def step_user_clears_all_tasks(context):
    clear_tasks()

@then('the to-do list should be empty')
def step_to_do_list_should_be_empty(context):
    tasks=load_tasks()
    assert len(tasks) == 0, "The to-do list is not empty after clearing"