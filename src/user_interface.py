from rich import table, console
# from rich.style import Style
# from rich.highlighter import RegexHighlighter
from rich.theme import Theme
# in hindsight, it may have been easier just to pretty print all this

from src.task_manager import TaskManager

# TODO: Add automated tests for the new UI behaviour.
#  At the moment the PR changes CLI output,
#  but there are no tests covering UserInterface.


class UserInterface:
    """
    Facilitates user interaction with the program using the command
    line interface.
    """
    def __init__(self):
        self.task_manager = TaskManager()
        self.rich_console = console.Console(
            highlight=True,
            theme=Theme(
                {"pending": "red",
                 "completed": "green"}
            )
        )
        self.task_table = self.create_table()

    def create_table(self):
        """
        Creates the table and populates it with tasks requested from
        the task manager class.

        Returns:
            Table: table with tasks.
        """
        new_table = table.Table(
            "Title",
            "Description",
            "Due Date",
            table.Column("Status", highlight=True),
            title="Tasks")
        for task in self.task_manager.tasks:
            new_table.add_row(
                task.title,
                task.description,
                task.due_date,
                task.status)
        return new_table

    def run(self):
        """
        Implements main loop of the user interface, accepts user input
        via the command line interface, and displays the task table.

        Returns:
            None
        """
        while True:
            self.rich_console.print("\nTask Manager CLI")
            self.rich_console.print("1. Add Task")
            self.rich_console.print("2. Delete Task")
            self.rich_console.print("3. List Tasks")
            self.rich_console.print("4. Exit")

            choice = input("Enter your choice: ")
            match choice:
                case "1":
                    title = input("Title: ")
                    description = input("Description: ")
                    due_date = input("Due Date (DD-MM-YYYY): ")
                    if self.task_manager.add_task(title,
                                                  description,
                                                  due_date
                                                  ):
                        for task in self.task_manager.tasks:
                            if task.title == title:
                                self.task_table.add_row(
                                    task.title,
                                    task.description,
                                    task.due_date,
                                    task.status
                                )
                        self.rich_console.print("Task Added")
                    else:
                        print("Something has gone wrong. Please try again.")
                case "2":
                    title = input("Title of the task to delete: ")
                    if self.task_manager.delete_task(title):
                        print("Task deleted successfully.")
                        self.task_table = self.create_table()
                    else:
                        print("Task not found.")
                case "3":
                    # Decided to still print empty table
                    # as this gives the user feedback
                    # that there *is* a table it's just empty
                    if len(self.task_manager.tasks) <= 0:
                        print("There are no tasks to display.")
                    self.rich_console.print(self.task_table)
                case "4":
                    print("Exiting Task Manager.")
                    break
                case _:
                    print("Invalid choice. Try again.")
