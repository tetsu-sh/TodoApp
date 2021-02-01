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
    a = "new"
    b = "wip"
    c = "done"

class Priority(enum.Enum):
    a = "low"
    b  = "middle"
    c = "high"