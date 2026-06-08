import unittest
# import requests
import os
from src.file_handler import IcsFileHandler
from src.task import Task

class TestIcsFileHandler(unittest.TestCase):
    def setUp(self):
        self.ICS = IcsFileHandler("ical_test.ics")

    def tearDown(self):
        # Clears test file without deleting.
        with open(self.ICS.target_file, "w"):
            pass

    def test_save_task(self):
        original_size = os.path.getsize(self.ICS.target_file)
        self.ICS.save_tasks(tasks =[
                Task("Task 1", "Description 1", "12-12-2024", "pending"),
                Task("Task 2", "Description 2", "15-12-2024", "completed"),
            ])
        self.assertLess(original_size, os.path.getsize(self.ICS.target_file))

    def test_load_tasks(self):
        sample_data = [
                Task("Task 1", "Description 1", "12-12-2024", "pending"),
                Task("Task 2", "Description 2", "15-12-2024", "completed"),
            ]
        self.ICS.save_tasks(tasks = sample_data)
        [task.to_dict() for task in sample_data]
        print(self.ICS.load_tasks())
        self.assertTrue([task.to_dict() in sample_data for task in self.ICS.load_tasks()])

    # KEEP FOR POSTERITY BUT LOAD TASKS TESTCASE SHOULD RAISE ERRORS IF ICS IS NOT VALID
    # def test_validate_ics(self):
    #     r = requests.get(url="https://icalendar.org/validator.html")
    #     self.assertTrue(r.status_code == 200, msg="Could not establish connection to validator")
    #     validation = requests.post(url="https://icalendar.org/validator.html#results", data=self.ICS.target_file)
    #     print(validation)
if __name__ == "__main__":
    unittest.main()