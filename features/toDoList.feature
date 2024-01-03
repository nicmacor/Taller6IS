Feature: To do list manager

    @toDoList
    Scenario: Add a task to the to-do list
    Given an empty to-do list
    | Task | Status|
    when the user adds a task "Buy groceries"
    Then the to-do list should contain "Buy groceries"
    | Task | Status |
    | Buy groceries | Incomplete |


    @toDoList
    Scenario: List all tasks in the to-do list
    Given the to-do list contains tasks
    | Task |
    | Buy groceries |
    | Pay bills |
    When the user list all tasks
    Then the output should contain
    To-Do List:
    1. Buy groceries - Incomplete
    2.- Pay bills - Incomplete


    @toDoList
    Scenario: Mark a task as completed
    Given the to-do list contains tasks:
    | Task | Status |
    | Buy groceries | Incomplete |
    When the user marks task "Buy groceries as completed
    Then the to-do list should show task "Buy groceries" as completed
    | Task | Status |
    | Buy groceries | Completed |


    @toDoList
    Scenario: Clear the entire to-do list
    Given the to-do list contains tasks
    | Task |
    | Buy groceries |
    | Pay bills |
    When the user clears the to-do list
    Then the to-do list should be empty
    | Task |
    And the following message should be displayed: To-do list cleared successfully!

    @toDoList
    Scenario: List all the Incomplete tasks in the to-do list
    Given the to-do list contains tasks
    | Task | Status |
    | Buy groceries | Completed |
    | Pay bills | Incompleted |
    When the user list all Incompleted tasks
    Then the output should contain
    To-Do List:
    2.- Pay bills - Incomplete

    @toDoList
    Scenario: Edit tasks in the to-do list
    Given the to-do list contains tasks
    