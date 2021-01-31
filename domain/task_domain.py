import enum

class Task:
    def __init__(self, task_id, task_name,status, priority,description,due_date) -> None:
        self.task_id = task_id
        self.task_name = task_name
        self.status = status
        self.priority = priority
        self.description  = description
        self.due_date = due_date

class Status(enum.Enum):
    new = 0
    wip = 1
    done = 2

class Priority(enum.Enum):
    low = 0
    middle  = 1
    high = 2