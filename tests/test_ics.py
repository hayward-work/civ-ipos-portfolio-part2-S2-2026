from src.file_handler import IcsFileHandler
from src.task import Task
IBS = IcsFileHandler("test_ical.ics")
IBS.save_tasks(tasks =[
        Task("Task 1", "Description 1", "12-12-2024", "pending"),
        Task("Task 2", "Description 2", "15-12-2024", "completed"),
    ])