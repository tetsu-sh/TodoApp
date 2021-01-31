from domain.task_domain import Task, Status, Priority
from domain.assign_domain import Assign
import uuid
from domain.interface_task_repository import ITaskRepository
from domain.interface_assign_repository import IAssignRepository

class TaskUsecase:
    def __init__(self, task_repository: ITaskRepository, assign_repository: IAssignRepository) -> None:
        self.task_repository = task_repository
        self.assign_repository = assign_repository

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
    
    def assign(self, task_id,user_id):
        assign_id = uuid.uuid4()
        assign = Assign(
            assign_id = assign_id,
            task_id = task_id,
            user_id = user_id
        )
        self.assign_repository.create(assign)
    
    def get_all_assign(self):
        assigns = self.assign_repository.load()
        return assigns
    
    def get_all_tasks_with_assign(self):
        tasks = self.get_all_tasks()
        assigns = self.get_all_assign()
        for assign in assigns:
            for task in tasks:
                if assign.task_id==task.task_id:
                    task["assigns"]=assign
        
        return tasks

        
class UserQuery:
    pass