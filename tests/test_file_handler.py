import unittest
import os
from src.file_handler import BinaryFileHandler
from src.task import Task

class TestBinaryFileHandler(unittest.TestCase):
    def setUp(self):
        self.BIN = BinaryFileHandler("bin_test.bin")

    def tearDown(self):
        # Clears test file without deleting.
        with open(self.BIN.target_file, "w"):
            pass

    def test_save_task(self):
        original_size = os.path.getsize(self.BIN.target_file)
        self.BIN.save_tasks(tasks =[
                Task("Task 1", "Description 1", "12-12-2024", "pending"),
                Task("Task 2", "Description 2", "15-12-2024", "completed"),
            ])
        self.assertLess(original_size, os.path.getsize(self.BIN.target_file))

    def test_load_tasks(self):
        sample_data = [
                Task("Task 1", "Description 1", "12-12-2024", "pending"),
                Task("Task 2", "Description 2", "15-12-2024", "completed"),
            ]
        self.BIN.save_tasks(tasks = sample_data)
        [task.to_dict() for task in sample_data]
        print(self.BIN.load_tasks())
        self.assertTrue([task.to_dict() in sample_data for task in self.BIN.load_tasks()])

if __name__ == "__main__":
    unittest.main()