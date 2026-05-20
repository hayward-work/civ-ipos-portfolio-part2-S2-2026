import unittest
from unittest.mock import patch
from src.task_manager import TaskManager
from src.task import Task


class TestTaskManager(unittest.TestCase):
    """
    Unit tests for Task Manager functionalities including adding, deleting, filtering,
    and persisting tasks to and from a binary file.
    """

    def setUp(self):
        """
        Set up the test environment by initialising a taskmanager
        object and backing up the original task binary file.
        """
        self.taskmanager = TaskManager()
        self.taskmanager.tasks = []

    def tearDown(self):
        """
        Clean up the test environment by removing any test-created binary files
        and restoring the original task binary file.
        """
        if self.taskmanager:
            for task in self.taskmanager.tasks:
                self.taskmanager.delete_task(task.title)

    @patch("src.file_handler.save_tasks")
    def test_add_task(self, patch):
        """
        Test adding a new task to the task list.
        Verify that the task is successfully added and the list size increases.
        """
        result = self.taskmanager.add_task("Test Task", "Description", "01-12-2024")
        print(self.taskmanager.tasks[0].description)
        self.assertTrue(result)
        self.assertEqual(len(self.taskmanager.tasks), 1)
        self.taskmanager.delete_task("Test Task")

    # @patch("src.file_handler.load_tasks")
    @patch("src.file_handler.save_tasks")
    def test_add_duplicate_task(self, patch):
        """
        Test adding a duplicate task with the same title.
        Verify that duplicates are not allowed and the function returns False.
        """
        self.taskmanager.add_task("Test Task", "New Description", "02-12-2024")
        result = self.taskmanager.add_task("Test Task", "Duplicate Task", "02-12-2024")
        self.assertFalse(result)
        self.taskmanager.delete_task("Test Task")

    # @patch("src.file_handler.load_tasks")
    @patch("src.file_handler.save_tasks")
    def test_add_invalid_due_date(self, patch):
        """
        Test adding a task with an invalid due date format.
        Verify that the function handles invalid input gracefully and returns False.
        """
        result = self.taskmanager.add_task("Test Task", "Description", "2024-12-01")
        self.assertFalse(result)
        self.taskmanager.delete_task("Test Task")

    @patch("src.file_handler.save_tasks")
    def test_delete_task(self, patch):
        """
        Test deleting a task by its title.
        Verify that the task is removed from the list and the list size decreases.
        """
        self.taskmanager.add_task("Task to Delete", "Description", "01-12-2024")
        result = self.taskmanager.delete_task("Task to Delete")
        self.assertTrue(result)
        self.assertEqual(len(self.taskmanager.tasks), 0)

    @patch("src.file_handler.save_tasks")
    def test_filter_tasks_by_status(self, patch):
        """
        Test filtering tasks based on their status (e.g., 'completed').
        Verify that only tasks matching the specified status are returned.
        """
        task1 = Task("Task 1", "Desc", "01-12-2024", "pending")
        task2 = Task("Task 2", "Desc", "02-12-2024", "completed")
        self.taskmanager.tasks.extend([task1, task2])
        filtered = self.taskmanager.filter_tasks_by_status("completed")
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0].title, "Task 2")


if __name__ == "__main__":
    unittest.main()
