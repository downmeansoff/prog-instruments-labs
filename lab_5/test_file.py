import pytest
from unittest.mock import MagicMock
from typing import List
from todo_manager import Task, TodoManager 

# tests for task class
def test_task_creation():
    task = Task(title="Test Task", description="Description of test task")
    assert task.title == "Test Task"
    assert task.description == "Description of test task"
    assert task.completed is False

def test_mark_complete():
    task = Task(title="Test Task", description="Test description")
    task.mark_complete()
    assert task.completed is True

# tests for TodoManager class
def test_add_task():
    manager = TodoManager()
    task = manager.add_task("Task 1", "Description 1")
    assert task in manager.tasks
    assert task.title == "Task 1"
    assert task.description == "Description 1"

def test_remove_task():
    manager = TodoManager()
    manager.add_task("Task to remove", "Description")
    assert manager.remove_task("Task to remove") is True
    assert not manager.find_task("Task to remove")

def test_find_task():
    manager = TodoManager()
    manager.add_task("Find me", "Find description")
    task = manager.find_task("Find me")
    assert task is not None
    assert task.title == "Find me"

def test_list_tasks():
    manager = TodoManager()
    manager.add_task("Task 1", "Description 1")
    manager.add_task("Task 2", "Description 2")
    tasks = manager.list_tasks()
    assert len(tasks) == 2
    assert tasks[0].title == "Task 1"
    assert tasks[1].title == "Task 2"

def test_clear_completed():
    manager = TodoManager()
    manager.add_task("Task 1", "Description 1")
    task = manager.add_task("Task 2", "Description 2")
    task.mark_complete()
    manager.clear_completed()
    tasks = manager.list_tasks()
    assert len(tasks) == 1
    assert tasks[0].title == "Task 1"

# add tasks
@pytest.mark.parametrize("title,description", [
    ("Task A", "Description A"),
    ("Task B", "Description B"),
    ("Task C", "Description C")
])
def test_add_task_parametrized(title, description):
    manager = TodoManager()
    task = manager.add_task(title, description)
    assert task.title == title
    assert task.description == description
    assert task in manager.tasks

def test_mark_task_complete_with_mock():
    manager = TodoManager()
    mock_task = MagicMock(spec=Task)
    mock_task.title = "Mock Task"
    manager.tasks.append(mock_task)

    result = manager.mark_task_complete("Mock Task")

    assert result is True
    mock_task.mark_complete.assert_called_once()

# Tasks to remove test
@pytest.mark.parametrize("tasks_to_add,tasks_to_remove,expected_remaining", [
    (["Task 1", "Task 2", "Task 3"], ["Task 2"], ["Task 1", "Task 3"]),
    (["Task A", "Task B"], ["Task A", "Task B"], []),
    (["Task X"], ["Task Y"], ["Task X"]),
])
def test_remove_tasks_parametrized(tasks_to_add, tasks_to_remove, expected_remaining):
    manager = TodoManager()
    for task in tasks_to_add:
        manager.add_task(task, "Some description")
    for task in tasks_to_remove:
        manager.remove_task(task)
    remaining_titles = [task.title for task in manager.list_tasks()]
    assert remaining_titles == expected_remaining