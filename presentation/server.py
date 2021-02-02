from usecase.user_usecase import UserUsecase
from infra.sqlite3.user_repository import UserRepository
from usecase.task_usecase import TaskUsecase
from infra.sqlite3.task_repository import TaskRepository
from infra.sqlite3.assign_repository import AssignRepository

from datetime import datetime, timedelta

from logging import getLogger
from common.logger import get_logger


logger = getLogger(__name__)
logger = get_logger(logger)

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

from domain.task_domain import Priority


app = FastAPI()


class User(BaseModel):
    user_name: str

    class Config:
        schema_extra = {
            "example":{
                "user_name":"test_user"
            }

        }

class Task(BaseModel):
    task_name: str
    priority: Priority
    description: str
    due_date: datetime

    class Config:
        schema_extra = {
            "example":{
                "task_name":"test_task",
                "priority": Priority("middle"),
                "description":"test_description",
                "due_date": datetime.now() + timedelta(days=2)
            }
        }

@app.post("/user")
def create_user(user: User):
    """
    ユーザ登録
    """
    user_repository = UserRepository()
    user_usecase = UserUsecase(user_repository)
    user_usecase.create_user(user.user_name)
    return


@app.get("/users")
def get_all_users():
    """
    ユーザ一覧
    """
    user_repository = UserRepository()
    user_usecase = UserUsecase(user_repository)
    users = user_usecase.get_all_users()
    response={
        "users":users
    }
    return response

@app.get("/user/tasks/undone/{user_id}")
def get_user_tasks_undone(user_id):
    """
    あるユーザが担当している未完了のタスクを一覧表示する。出力順は作業状態(作業中->未着手)及び、同じ作業状態であれば優先度の高い順とする。
    """
    user_repository = UserRepository()
    user_usecase = UserUsecase(user_repository)
    tasks = user_usecase.get_user_task_undone(user_id)
    response={
        "tasks":tasks
    }
    return response

@app.delete("/user/{user_id}")
def delete_user(user_id):
    """
    ユーザ削除
    """
    user_repository = UserRepository()
    user_usecase = UserUsecase(user_repository)
    user_usecase.delete_user(user_id)
    return


@app.post("/task")
def create_task(task: Task):
    """
    タスク登録する
    """
    task_repository = TaskRepository()
    assign_repository = AssignRepository()
    task_usecase = TaskUsecase(task_repository, assign_repository)
    task_usecase.create_task(task.task_name, task.priority, task.description,task.due_date)


    return

@app.get("/tasks")
def get_all_tasks():
    """
    タスク一覧を取得
    """
    task_repository = TaskRepository()
    assign_repository = AssignRepository()
    task_usecase = TaskUsecase(task_repository, assign_repository)
    tasks = task_usecase.get_all_tasks()

    response={
        "tasks":tasks
    }
    return response

@app.post("/task/wip/{task_id}")
def task_wip(task_id):
    """
    タスクの状態を作業中にする
    """
    task_repository = TaskRepository()
    assign_repository = AssignRepository()
    task_usecase = TaskUsecase(task_repository, assign_repository)
    task_usecase.task_status_wip(task_id)
    
    return

@app.post("/task/done/{task_id}")
def task_done(task_id):
    """
    タスクの状態を完了にする
    """
    task_repository = TaskRepository()
    assign_repository = AssignRepository()
    task_usecase = TaskUsecase(task_repository, assign_repository)
    task_usecase.task_status_done(task_id)
    
    return


@app.post("/assign/{task_id}/{user_id}")
def assign(task_id,user_id):
    """
    タスクをユーザにアサインする(アサインを外す・アサインを更新する機能は必須ではないものとする)
    """
    task_repository = TaskRepository()
    assign_repository = AssignRepository()
    task_usecase = TaskUsecase(task_repository, assign_repository)
    task_usecase.assign(task_id,user_id)
    
    return

@app.get("/tasks/undone")
def get_tasks_undone():
    """
    未完了タスクの一覧表示。出力順は作業状態(作業中->未着手)及び、同じ作業状態であれば優先度の高い順とする。
    """
    task_repository = TaskRepository()
    assign_repository = AssignRepository()
    task_usecase = TaskUsecase(task_repository, assign_repository)
    tasks = task_usecase.get_all_tasks_undone()

    response={
        "tasks":tasks
    }
    return response

@app.get("/tasks/noassign")
def get_tasks_noassign():
    """
    誰にもアサインされていない未完了タスクを一覧表示する。出力順は優先度の高い順とする。
    """
    task_repository = TaskRepository()
    assign_repository = AssignRepository()
    task_usecase = TaskUsecase(task_repository, assign_repository)
    tasks = task_usecase.get_all_tasks_with_noassign()

    response={
        "tasks":tasks
    }
    return response

@app.get("/users/wip/count")
def get_users_wip_count():
    """
    ユーザごとのアサインされている作業中タスクの数。優先順位別にカウントして表示する。
    """
    user_repository = UserRepository()
    user_usecase = UserUsecase(user_repository)
    users = user_usecase.get_users_wip_count()

    response={
        "users":users
    }
    return response

@app.get("/usrs/done/count")
def get_users_done_count():
    """
    多くのタスクを完了させたユーザのランキング。（二人以上で担当していた場合には、それぞれのユーザに対してタスク完了数を１つ足すものとする）
    """
    user_repository = UserRepository()
    user_usecase = UserUsecase(user_repository)
    users = user_usecase.get_users_done_count()

    response={
        "users":users
    }
    return response
