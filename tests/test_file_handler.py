import unittest
import os
import unittest
from src.file_handler import FileHandler
from src.task import Task


class TestFileHandler(unittest.TestCase):
    def setUp(self):
        self.file_handler = FileHandler()
        self.sample_tasks = [
            Task("Task 1", "Description 1", "12-12-2024", "pending"),
            Task("Task 2", "Description 2", "15-12-2024", "completed"),
        ]

    def tearDown(self) -> None:
        if os.path.exists("tasks.bin"):
            os.remove("tasks.bin")

    def test_load_tasks(self) -> None:
        """
        Test the binary file content by loading tasks
        from an empty file to verify the file is empty
        by comparing the contents of the file to the sample data,
        then save the sample data to the file and verify that the
        loaded data now matches the sample data.
        Returns
            None
        """
        (self.assertNotEqual(
            [task.to_dict() for task in self.file_handler.load_tasks()],
            [task.to_dict() for task in self.sample_tasks]
        ) and self.assertTrue(len(self.file_handler.load_tasks()) == 0))
        self.file_handler.save_tasks(self.sample_tasks)
        self.assertEqual([task.to_dict() for task in self.file_handler.load_tasks()],
                         [task.to_dict() for task in self.sample_tasks])

    def test_save_tasks(self) -> None:
        """
        Test binary file saving by comparing the size
        of a binary file saved to with an empty list
        to one which has been saved to with the sample data.
        Returns:
            None
        """
        self.file_handler.save_tasks([])
        original_size = os.path.getsize("tasks.bin")
        self.file_handler.save_tasks(self.sample_tasks)
        self.assertLess(original_size, os.path.getsize("tasks.bin"))


if __name__ == "__main__":
    unittest.main()
