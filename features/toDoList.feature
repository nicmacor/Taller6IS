Feature: To do list manager

    Scenario: Add a task to the to-do list
        Given an empty to-do list
        when the user adds a task "Buy groceries" with description "Snacks and food"
        Then the to-do list should contain "Buy groceries"

    Scenario: List all tasks in the to-do list
        Given the to-do list contains tasks
        When the user list all tasks
        Then the output should contain all tasks
    
    Scenario: Mark a task as completed
        Given the to-do list contains tasks
        When the user marks task "1" as completed
        Then the to-do list should show task "1" as completed

    
    Scenario: List all the Incomplete tasks in the to-do list
        Given the to-do list contains tasks
        When the user list all incompleted tasks
        Then the output should contain all incompleted tasks

    
    Scenario: Edit tasks in the to-do list
        Given the to-do list contains tasks
        When the user edits task "1" to "Exercise" and "Hacer ejercicio"
        Then the name and description of task "1" should be updated
    
    Scenario: Clear the entire to-do list
        Given the to-do list contains tasks
        When the user clears the to-do list
        Then the to-do list should be empty
    