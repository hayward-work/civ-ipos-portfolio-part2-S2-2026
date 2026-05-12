import pickle
import os

TASK_FILE = "tasks.bin"


class FileHandler:
    def __init__(self, task_file: str = TASK_FILE):
        self.task_file = task_file

    def load_tasks(self):
        """
        Load tasks from a binary file using the pickle module.

        Returns:
            list: A list of Task objects loaded from the binary file.
                  If the file does not exist, an empty list is returned.
        """
        if os.path.exists(self.task_file):
            with open(self.task_file, "rb") as file:
                return pickle.load(file)
        return []


    def save_tasks(self, tasks):
        """
        Save a list of tasks to a binary file using the pickle module.

        Args:
            tasks (list): A list of Task objects to be saved to the file.

        Side Effects:
            - Writes the serialized task list to TASK_FILE.
            - Overwrites the file if it already exists.
        """
        with open(self.task_file, "wb") as file:
            pickle.dump(tasks, file)
