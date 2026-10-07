import tempfile
import unittest
from src.file_handler import FileHandler
from src.task import Task


class TestFileHandler(unittest.TestCase):
    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(
            suffix=".bin",
            delete=True,
            delete_on_close=False
        )
        # technically doesn't need to be .bin
        # but if the file isn't cleaned up properly
        # this makes the cause more obvious
        self.file_handler = FileHandler(task_file=self.temp_file.name)
        self.sample_tasks = [
            Task("Task 1", "Description 1", "12-12-2024", "pending"),
            Task("Task 2", "Description 2", "15-12-2024", "completed"),
        ]

    def tearDown(self) -> None:
        self.temp_file.close()

    def test_file_handler(self) -> None:
        """
        Test that the load method correctly raises an end of file
        error when loading from an empty file, then save sample data
        to the file, then reload the tasks back from the file to
        check that file is no longer empty and that the returned
        data matches the inputted sample data.
        Returns:
            None
        """
        # I originally had test save file and test load file split up
        # but their functionality is basically inseparable.
        # The file_save method is so basic
        # that any other way of populating a file with data
        # is effectively just reimplementing the method.
        # Likewise for loading.
        #
        # Also this docstring is somewhat weak.
        with self.assertRaises(EOFError):
            self.file_handler.load_tasks()
        self.file_handler.save_tasks(self.sample_tasks)
        self.assertEqual([task.to_dict() for task in self.file_handler.load_tasks()],
                         [task.to_dict() for task in self.sample_tasks])

    # def test_save_tasks(self) -> None:
    #     """
    #     Test binary file saving by comparing the size
    #     of a binary file saved to with an empty list
    #     to one which has been saved to with the sample data.
    #     Returns:
    #         None
    #     """
    #     # self.file_handler.save_tasks([])
    #     # original_size = os.path.getsize("tasks.bin")
    #     # self.file_handler.save_tasks(self.sample_tasks)
    #     # self.assertLess(original_size, os.path.getsize("tasks.bin"))


if __name__ == "__main__":
    unittest.main()
