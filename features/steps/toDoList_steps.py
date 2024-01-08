from behave import given, when, then
from toDoList import ToDoList

toDoList=ToDoList()

#1.The user wants to add a task

@given('an empty to-do list')
def step_add_task(context):
    pass

@when('the user adds a task "{name}" with description "{description}"')
def step_add_task_name_with_description(context, name, description):
    toDoList.add_task(name, description)

@then('the to-do list should contain "{name}"')
def step_task_should_be_added_to_to_do_list(context, name):
    task = toDoList.get_task(name)
    assert task is not None, f"Task '{name} was not added to the to-do list"


@given('the to-do list contains tasks')
def step_to_do_list_contains_task(context):
    toDoList.add_task("Buy groceries", "Buy food and snacks")
    toDoList.add_task("Pay bills", "Pay rent and ensurance")


#3.The user marks a task as completed
@when('the user marks task "{task_index:d}" as completed')
def step_user_marks_task_completed(context, task_index):
    toDoList.mark_complete(task_index)

@then('the to-do list should show task "{task_index:d}" as completed')
def step_impl(context, task_index):
    task= toDoList.tasks[task_index-1]
    assert task.status == 'Completed', f"Task {task_index} was not marked as completed"

#4. The user wants to list the incompleted tasks
@when('the user list all incompleted tasks')
def step_user_list_all_incompleted_tasks(context):
    context.list_incomplete_output = toDoList.list_incomplete_tasks()

@then('the output should contain all incompleted tasks')
def step_output_contain_incompleted_tasks(context):
    assert context.list_incomplete_output is not None , "No tasks were listed"

##2.List the tasks in the to-do List
@when('the user list all tasks')
def step_list_all_tasks(context):
    context.listOutput = toDoList.list_tasks()

@then('the output should contain all tasks')
def step_output_contain_all_tasks(context):
    assert context.listOutput is not None, f"No tasks were listed"

#5.The user edits a task in the to-do list

@when('the user edits task "{task_index:d}" to "{new_name}" and "{new_description}"')
def step_edit_task(context, task_index, new_name, new_description):
    context.new_name=new_name
    context.new_description=new_description
    toDoList.edit_task(task_index, new_name, new_description)

@then('the name and description of task "{task_index:d}" should be updated')
def step_task_edited_updated(context, task_index):
    task = toDoList.tasks[task_index-1]
    assert context.new_name == task.name, f"Description of task '{task_index}' was not updated as expected to '{context.new_description}'"

#6. the user clears all tasks
@when('the user clears the to-do list')
def step_clear_to_do_list(context):
    toDoList.clear_tasks()

@then('the to-do list should be empty')
def step_to_do_list_cleared(context):
    assert len(toDoList.tasks) == 0, "The to-do list is not empty after clearing"
