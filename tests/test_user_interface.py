import unittest
from io import StringIO
from unittest.mock import patch
from src.user_interface import UserInterface


@patch(target='src.task_manager.save_tasks', autospec=True)
@patch(target='src.task_manager.load_tasks', autospec=True, return_value=None)
class TestUserInterface(unittest.TestCase):
    """
    Unit tests for using user interface class over console for
    input and output.
    """

    def setUp(self):
        """
        Set up the test environment by initialising a user interface object.
        """
        self.ui = UserInterface()
        # I hate this but patches don't get applied during setup and fixing
        # the code that causes this to have files in it is out of scope of
        # this issue.

        # Basically since the task manager tests don't clean up after
        # themselves, it leaves behind a tasks.bin file that gets read from
        # during the UI class' construction when creating the rich table
        self.ui.task_manager.tasks = []
        self.ui.task_table = self.ui.create_table()

    def tearDown(self):
        """
        Clean up the test environment by setting
        the user interface instance to none.
        """
        self.ui = None

    @patch('src.user_interface.input', create=True)
    def test_run_user_interface(self, mock_input, patch_save_task, patch_load_task):

        # Better to create a new output var for each test
        # to avoid accidental cross contamination
        output = StringIO()
        self.ui.rich_console.file = output
        # This allows me to queue inputs using a python list
        mock_input.side_effect = ["4"]
        self.ui.run()
        self.assertIn(
            "\nTask Manager CLI\n"
            "1. Add Task\n"
            "2. Delete Task\n"
            "3. List Tasks\n"
            "4. Exit",
            output.getvalue())
        # # proof everything works, remove later
        # print(output.getvalue())

        # Should look something like this:
        #     Task
        #     Manager
        #     CLI
        #     1.
        #     Add
        #     Task
        #     2.
        #     Delete
        #     Task
        #     3.
        #     List
        #     Tasks
        #     4.
        #     Exit
        #     Tasks
        #
        # ┏━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━┓
        # ┃ Title     ┃ Description ┃ Due
        # Date   ┃ Status  ┃
        # ┡━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━┩
        # │ Test
        # Task │ Description │ 01 - 12 - 2024 │ pending │
        # └───────────┴─────────────┴────────────┴─────────┘
        #
        # Task
        # Manager
        # CLI
        # 1.
        # Add
        # Task
        # 2.
        # Delete
        # Task
        # 3.
        # List
        # Tasks
        # 4.
        # Exit

    # result = self.taskmanager.add_task()
    # print(self.taskmanager.tasks[0].description)
    # self.assertTrue(result)
    # self.assertEqual(len(self.taskmanager.tasks), 1)
    # self.taskmanager.delete_task("Test Task")

    # Patch prevents making a task file,
    # will need changing when working with filehandler as class

    @patch('src.user_interface.input', create=True)
    def test_add_task_to_table(self, mock_input, patch_save_task, patch_load_task):
        """
        Test adding a task to the task list and listing task table.
        """
        output = StringIO()
        self.ui.rich_console.file = output
        mock_input.side_effect = ["3",
                                  "1",
                                  "Test Task",
                                  "Description",
                                  "01-12-2024",
                                  "3",
                                  "4"]
        self.ui.run()
        # This is probably bad practice but I'm lazy so it's staying in.
        self.assertRegex(output.getvalue(), "("
                                            "(There are no tasks to display)"
                                            "(\n|.)*"
                                            "(Test Task)"
                                            "(\n|.)*"
                                            "(Description)"
                                            "(\n|.)*"
                                            "(01-12-2024)"
                                            ")"
                         )
        # self.assertIn(["There are no tasks to display." and
        #               "Test Task" and
        #               "Description" and
        #               "01-12-2024",
        #               output.getvalue())


if __name__ == "__main__":
    unittest.main()
