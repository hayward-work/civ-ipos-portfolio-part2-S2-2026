import pickle
import os
from abc import ABC, abstractmethod


class FileHandler(ABC):
    def __init__(self, filepath: str) -> None:
        self.target_file = filepath

    @abstractmethod
    def load_tasks(self):
        pass

    @abstractmethod
    def save_tasks(self, tasks):
        pass


class BinaryFileHandler(FileHandler):
    def load_tasks(self):
        """
        Load tasks from a binary file using the pickle module.

        Returns:
            list: A list of Task objects loaded from the binary file.
                  If the file does not exist, an empty list is returned.
        """
        if os.path.exists(self.target_file):
            with open(self.target_file, "rb") as file:
                return pickle.load(file)
        return []


    def save_tasks(self, tasks):
        """
        Save a list of tasks to a binary file using the pickle module.

        Side Effects:
            - Writes the serialized task list to TASK_FILE.
            - Overwrites the file if it already exists.
        """
        with open(self.target_file, "wb") as file:
            # noinspection PyTypeChecker
            #
            # This feels wrong but according to
            # stack overflow it's a pycharm specific issue:
            # https://stackoverflow.com/questions/79049420/
            pickle.dump(tasks, file)
