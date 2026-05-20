from src.task import Task
from src.file_handler import load_tasks, save_tasks
from datetime import datetime

# TODO: Fix the incorrect docstrings in src/task_manager.py
#  so they match the current class methods and parameters.


class TaskManager:

    def __init__(self):
        self.tasks = []
        self.update_tasks()

    def update_tasks(self):
        self.tasks = load_tasks()

    def add_task(self, title, description, due_date):
        """
        Add a new task to the task list.

        Args:
            title (str): The title of the new task.
            description (str): A brief description of the task.
            due_date (str): The due date of the task in 'DD-MM-YYYY'
            format.

        Returns:
            bool: True if the task is added successfully,
            False otherwise.

        Raises:
            ValueError: If the due date is not in the correct format.

        Side Effects:list_tasks(self.tasks)
            - Saves the updated task list to a file using `save_tasks`.
        """
        # Prevent duplicate tasks
        if any(task.title == title for task in self.tasks):
            print("Error: A task with this title already exists.")
            return False

        # Validate due date format
        try:
            datetime.strptime(due_date, "%d-%m-%Y")
        except ValueError:
            print("Error: Invalid date format. Use DD-MM-YYYY.")
            return False

        self.tasks.append(Task(title, description, due_date))
        save_tasks(self.tasks)
        return True

    def delete_task(self, title):
        """
        Delete a task from the task list based on its title.

        Args:
            title (str): The title of the task to be deleted.

        Returns:
            bool: True if the task was found and deleted, False otherwise.

        Side Effects:
            - Saves the updated task list to a file using save_tasks`.
        """
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                save_tasks(self.tasks)
                return True
        return False

    def filter_tasks_by_status(self, status):
        """
        Filter tasks by their status.

        Args:
            status (str): The status to filter tasks by
            (e.g., "pending" or "completed").

        Returns:
            list: A list of Task objects that match the specified status.
        """
        return [task for task in self.tasks if task.status == status]
