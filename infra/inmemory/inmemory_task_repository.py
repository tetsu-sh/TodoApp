from domain.interface_task_repository import ITaskRepository
from domain.task_domain import Task
import uuid

class InmemoryTaskRepository(ITaskRepository):
    def __init__(self):
        self.data = []

    def create(self, task:Task):
        new_task = {
            "task_id" :task.task_id,
            "task_name": task.task_name,
            "status":task.status,
            "priority":task.priority,
            "description":task.description,
            "due_date":task.due_date
        }
        self.data.append(new_task)
        return

    def load(self):
        return self.data

    def find(self, task_id):
        res = [k for k ,v in self.data.items() if v==task_id]

        return res
    
    def update_status(self, task_id, status):
        new_tasks =[]
        for task in self.data:
            if task["task_id"]==task_id:
                task["status"] = status
            new_tasks.append(task)
        self.data = new_tasks

    def delete(self, task_id):
        pass