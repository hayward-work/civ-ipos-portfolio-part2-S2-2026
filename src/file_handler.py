import pickle
import os
from datetime import date, datetime
# TODO: REMOVE THIS

import icalendar
from abc import ABC, abstractmethod

from icalendar.attr import status_property


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
            - Writes the serialized task list to self.filepath.
            - Overwrites the file if it already exists.
        """
        with open(self.target_file, "wb") as file:
            # noinspection PyTypeChecker
            #
            # This feels wrong but according to
            # stack overflow it's a pycharm specific issue:
            # https://stackoverflow.com/questions/79049420/
            pickle.dump(tasks, file)

class IcsFileHandler(FileHandler):
    def __init__(self, filepath: str):
        super().__init__(filepath)
        # TODO: REWRITE THIS SO CALENDAR IS CREATED IN SAVE TASKS METHOD
        self.calender = icalendar.Calendar()
        self.calender.add("prodid", "https://github.com/NM-TAFE/at2-portfolio-por-part-2-hayward-work/")
        self.calender.add("version", "2.0")
        self.calender.add("summary", "Task tracker")

    def load_tasks(self):
        """
        Loads tasks from .ics file and returns it as a list of tasks.

        Returns:
            list: A list of Task objects loaded from the iCal .ics file.
                If the file does not exist, an empty list is returned.
        """

    def save_tasks(self, tasks):
        """
        Save a list of tasks to an iCal file using the icalendar module.

        Side Effects:
            - Writes the task list to self.filepath in a way that;s.
            - Overwrites the file if it already exists.
        """
        # [icalendar.Calendar(task.to_dict()) for task in tasks]
        # print([task.to_ical() for task in tasks])
        # TODO: use status as iCal status property, description as ical description property, due date as due, and title as summary
        # vtodos would be perfect however they are not widely supported, implementation using todos passes ical verifier however is incompatible with most calendars
        todo_status_dict = {"pending": "IN-PROCESS",
                       "completed": "COMPLETED"}
        for task in tasks:
            task_dict = task.to_dict()
            todo = icalendar.Todo()
            todo.add('dtstamp', datetime.now())
            # Title is used as unique identifier for tasks elsewhere
            # in the program, making it a good choice for a unique id
            todo.add('uid', hash(task_dict["title"]))
            todo.add('summary', task_dict["title"])
            todo.add('description', task_dict["description"])
            todo.add('due', datetime.strptime(task_dict["due_date"], "%d-%m-%Y"))

            todo.add('status', todo_status_dict[task_dict["status"]])
            self.calender.add_component(todo)
        with open(self.target_file, "wb") as file:
        # noinspection PyTypeChecker
            file.write(self.calender.to_ical())
