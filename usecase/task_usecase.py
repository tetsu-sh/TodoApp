from domain.task_domain import Task, Status, Priority
from domain.assign_domain import Assign
import uuid
from operator import itemgetter
from domain.interface_task_repository import ITaskRepository
from domain.interface_assign_repository import IAssignRepository
from infra.sqlite3.task_repository import TaskQuery

class TaskUsecase:
    def __init__(self, task_repository: ITaskRepository, assign_repository: IAssignRepository) -> None:
        self.task_repository = task_repository
        self.assign_repository = assign_repository

    def create_task(self,task_name,priority,description,due_date):
        """
        タスク登録する
        """
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
        """
        タスクの状態を作業中にする
        """
        self.task_repository.update_status(task_id, Status(1))
        return
    
    def task_status_done(self, task_id):
        """
        タスクの状態を完了にする
        """
        self.task_repository.update_status(task_id, Status(2))
        return
    
    def assign(self, task_id,user_id):
        """
        タスクをユーザにアサインする(アサインを外す・アサインを更新する機能は必須ではないものとする)
        """
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

    def get_all_tasks_undone(self):
        """
        未完了タスクの一覧表示。出力順は作業状態(作業中->未着手)及び、同じ作業状態であれば優先度の高い順とする。
        """
        query = TaskQuery()
        tasks = query.query_tasks_status_undone()
        # print(tasks)
        # sorted_tasks = sorted(tasks, key=itemgetter("status", "priority"))
        return tasks
    
    def get_all_tasks_with_noassign(self):
        """
        誰にもアサインされていない未完了タスクを一覧表示する。出力順は優先度の高い順とする。
        """
        # tasks = self.get_all_tasks_undone()
        # assigns = self.get_all_assign()
        # tasks_noassign = []
        # for task in tasks:
        #     for assign in assigns:
        #         if task.task_id==assign.task_id:
        #             tasks.remove(task)
        #             break
        query = TaskQuery()
        tasks = query.query_tasks_with_noassign()
        
        return tasks

        
class UserQuery:
    pass