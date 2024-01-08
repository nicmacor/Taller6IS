Feature: To do list manager

    Scenario: Add a task to the to-do list
        Given an empty to-do list
        | Task | Status|
        when the user adds a task "Buy groceries" with description "Snacks and food"
        Then the to-do list should contain "Buy groceries"
        | Task | Status |
        | Buy groceries | Incomplete |

    Scenario: List all tasks in the to-do list
        Given the to-do list contains tasks
        | Task |
        | Buy groceries |
        | Pay bills |
        When the user list all tasks
        Then the output should contain all tasks
        """
        To-Do List:
        1. Buy groceries - Incomplete
        2.- Pay bills - Incomplete
        """
    
    Scenario: Mark a task as completed
        Given the to-do list contains tasks
        | Task | Status |
        | Buy groceries | Incomplete |
        When the user marks task "1" as completed
        Then the to-do list should show task "1" as Completed
        | Task | Status |
        | Buy groceries | Completed |
    
    Scenario: List all the Incomplete tasks in the to-do list
        Given the to-do list contains tasks
        | Task | Status |
        | Buy groceries | Completed |
        | Pay bills | Incompleted |
        When the user list all incompleted tasks
        Then the output should contain all incompleted tasks
        """
        To-Do List:
        2.- Pay bills - Incomplete
        """
    
    Scenario: Edit tasks in the to-do list
        Given the to-do list contains tasks
        """
        To-Do List:
        1. Buy groceries - Incomplete
        2.- Pay bills - Incomplete
        """
        When the user edits task "1" to "Exercise" and "Hacer ejercicio"
        Then the name and description of task "1" should be updated
        """
        To-Do List:
        1. Exercise - Incomplete
        2.- Pay bills - Incomplete
        """
    
    Scenario: Clear the entire to-do list
        Given the to-do list contains tasks
        | Task |
        | Buy groceries |
        | Pay bills |
        When the user clears the to-do list
        Then the to-do list should be empty
        | Task |
    