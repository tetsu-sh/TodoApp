from domain.task_domain import Task, Status, Priority
import uuid
from domain.interface_task_repository import ITaskRepository

class TaskUsecase:
    def __init__(self, task_repository: ITaskRepository) -> None:
        self.task_repository = task_repository

    def create_task(self,task_name,priority,description,due_date):
        task_id = uuid.uuid4()
        user = Task(
            task_id = task_id, 
            task_name = task_name, 
            status=Status(0), 
            priority=Priority(priority),
            description=description,
            due_date=due_date
            )
        self.task_repository.create(user)
        return

    def get_all_tasks(self):
        tasks = self.task_repository.load()
        return tasks
    
    def task_status_wip(self, task_id):
        self.task_repository.update_status(task_id, Status(1))
        return
    
    def task_status_done(self, task_id):
        self.task_repository.update_status(task_id, Status(2))
        return
        
class UserQuery:
    pass