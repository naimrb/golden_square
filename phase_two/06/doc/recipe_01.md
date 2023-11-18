# tasks.py

## 1. Describe the Problem
As a user\
So that I can keep track of my tasks\
I want a program that I can add todo tasks to and see a list of them.

As a user\
So that I can focus on tasks to complete\
I want to mark tasks as complete and have them disappear from the list.

## 2. Design the Function Signature

```python
class TaskTracker():
    def __init__(self):
    """
    Parameters:
        tasks: an empty list

    Returns: 
        nothing
    """
    def add(self, task):
    """
    Parameters:
        task: a string that contains the todo task

    Returns: 
        nothing
    """
    def list(self):
    """
    Parameters:
        none

    Returns: 
        self.tasks: which contains all the todo tasks
    """
    def completed(self, task)
    """
    Parameters:
        task: a string that contains the completed task

    Returns: 
        nothing
    """
```

## 3. Create Examples as Tests


```python
"""
Check initalization of the instance 
"""
tracker = TaskTracker()
isinstance(tracker, TaskTracker) => True

"""
Given a todo task it will store it in the tasks list 
"""
tracker.add("Cleaning")
tracker.tasks => ['Cleaning']

"""
Calling the list() method it will return us the tasks list
"""
tracker.list() => ['Cleaning']

"""
Given a completed task it will remove it from the tasks list
"""
tracker.completed('Cleaning')
tracker.tasks => []
```