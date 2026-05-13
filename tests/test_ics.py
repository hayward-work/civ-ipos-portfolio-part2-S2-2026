import unittest
import requests
from src.file_handler import IcsFileHandler
from src.task import Task

class TestIcsFileHandler(unittest.TestCase):
    def setUp(self):
        self.ICS = IcsFileHandler("test_ical.ics")

    def test_save_task(self):
        self.ICS.save_tasks(tasks =[
                Task("Task 1", "Description 1", "12-12-2024", "pending"),
                Task("Task 2", "Description 2", "15-12-2024", "completed"),
            ])


    def test_validate_ics(self):
        r = requests.get(url="https://icalendar.org/validator.html")
        self.assertTrue(r.status_code == 200, msg="Could not establish connection to validator")
        validation = requests.post(url="https://icalendar.org/validator.html#results", data=self.ICS.target_file)
