from loguru import logger as log
import unittest
from src.task_manager import add_task, delete_task, filter_tasks_by_status
from src.file_handler import save_tasks, load_tasks
from src.task import Task
import os

TEST_FILE = "test_tasks.bin"
TEST_LOGGER = "test_logger.txt"


class TestLogger(unittest.TestCase):
    """
    Unit tests for Logging Functionality provided and implemented by LogGuru
    """

    def setUp(self):
        """
        Set up the test environment by initialising an empty log file,
        backing up the original log file, and for the sake of testing,
        initializing an empty task list, and backing up the original
        task binary file.
        """
        self.tasks = []
        self.original_file = "tasks.bin"
        self.original_log = "log.txt"
        if os.path.exists(TEST_FILE):
            os.remove(TEST_FILE)
        os.rename("tasks.bin", TEST_FILE) if os.path.exists("tasks.bin") else None
        if os.path.exists(TEST_LOGGER):
            os.remove(TEST_LOGGER)
        os.rename("log.txt", TEST_FILE) if os.path.exists("log.txt") else None

    def tearDown(self):
        """
        Clean up the test environment by removing any test-created files
        and restoring the originals.
        """
        if os.path.exists("tasks.bin"):
            os.remove("tasks.bin")
        os.rename(TEST_FILE, "tasks.bin") if os.path.exists(TEST_FILE) else None
        if os.path.exists("log.txt"):
            os.remove("log.txt")
        os.rename(TEST_LOGGER, "tasks.txt") if os.path.exists(TEST_LOGGER) else None



if __name__ == "__main__":
    unittest.main()
