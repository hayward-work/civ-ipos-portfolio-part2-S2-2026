from rich import table, console
# from rich.style import Style
# from rich.highlighter import RegexHighlighter
# from rich.theme import Theme
# in hindsight, it may have been easier just to pretty print all the table stuff

from src.task_manager import TaskManager as task_manager

class UserInterface:
    """
    Facilitates user interaction with the program using the command
    line interface.
    """
    def __init__(self):
        # class RegexPatterns(RegexHighlighter):
        #     base_style = Style()
        #     highlights = [r"pending, completed"]
        self.rich_console = console.Console(highlight=True)
        self.task_table = self.create_table()


    def create_table(self):
        """
        Creates the table and populates it with tasks requested from
        the task manager class.

        Returns:
            Table: table with tasks.
        """
        new_table = table.Table("Title", "Description", "Due Date", table.Column("Status", highlight=True), title="Tasks")
        for task in task_manager.tasks:
            # TODO: resolve colours having no effect.
            status = "[red]Pending" if task.status == "pending" else "[green]Completed"
            print(status)
            new_table.add_row(task.title, task.description, task.due_date, status)
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
                    task_manager.add_task(title, description, due_date)
                    for task in task_manager.tasks:
                        if task.title == title:
                            self.task_table.add_row(task.title, task.description, task.due_date, task.status)
                    self.rich_console.print("Task Added")
                case "2":
                    title = input("Title of the task to delete: ")
                    if task_manager.delete_task(title):
                        print("Task deleted successfully.")
                        self.task_table = self.create_table()
                    else:
                        print("Task not found.")
                case "3":
                    # Decided to still print empty table
                    # as this gives the user feedback
                    # that there *is* a table it's just empty
                    if len(task_manager.tasks) <= 0: print("There are no tasks to display.")
                    self.rich_console.print(self.task_table)
                case "4":
                    print("Exiting Task Manager.")
                    break
                case _:
                    print("Invalid choice. Try again.")