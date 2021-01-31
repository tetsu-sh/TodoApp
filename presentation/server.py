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
    priority: int
    description: str
    due_date: datetime

    class Config:
        schema_extra = {
            "example":{
                "task_name":"test_task",
                "priority": 1,
                "description":"test_description",
                "due_date": datetime.now() + timedelta(days=2)
            }
        }

@app.post("/user")
def create_user(user: User):
    logger.info("start create user")


    user_repository = UserRepository()
    user_usecase = UserUsecase(user_repository)
    user_usecase.create_user(user.user_name)

    message = {"message": "success"}
    return message


@app.get("/users")
def get_all_users():
    user_repository = UserRepository()
    user_usecase = UserUsecase(user_repository)
    users = user_usecase.get_all_users()
    response={
        "users":users
    }
    return response

@app.get("/user/tasks/{user_id}")
def get_user_tasks(user_id):
    user_repository = UserRepository()
    user_usecase = UserUsecase(user_repository)
    tasks = user_usecase.get_user_task(user_id)
    response={
        "tasks":tasks
    }
    return response

@app.delete("/user/{user_id}")
def delete_user(user_id):
    user_repository = UserRepository()
    user_usecase = UserUsecase(user_repository)
    user_usecase.delete_user(user_id)

    message = {"message": "success"}
    return message


@app.post("/task")
def create_task(task: Task):
    logger.info("start create task")


    task_repository = TaskRepository()
    assign_repository = AssignRepository()
    task_usecase = TaskUsecase(task_repository, assign_repository)
    task_usecase.create_task(task.task_name, task.priority, task.description,task.due_date)

    message = {"message": "success"}
    return message

@app.get("/tasks")
def get_all_tasks():
    logger.info("start create task")


    task_repository = TaskRepository()
    assign_repository = AssignRepository()
    task_usecase = TaskUsecase(task_repository, assign_repository)
    tasks = task_usecase.get_all_tasks()

    response={
        "tasks":tasks
    }
    return response

@app.post("/task-wip/{task_id}")
def task_wip(task_id):
    logger.info("start create task")


    task_repository = TaskRepository()
    assign_repository = AssignRepository()
    task_usecase = TaskUsecase(task_repository, assign_repository)
    task_usecase.task_status_wip(task_id)

    message = {"message": "success"}
    return message

@app.post("/task-done/{task_id}")
def task_done(task_id):
    logger.info("start create task")


    task_repository = TaskRepository()
    assign_repository = AssignRepository()
    task_usecase = TaskUsecase(task_repository, assign_repository)
    task_usecase.task_status_done(task_id)

    message = {"message": "success"}
    return message


@app.post("/assign/{task_id}/{user_id}")
def assign(task_id,user_id):
    logger.info("start create task")


    task_repository = TaskRepository()
    assign_repository = AssignRepository()
    task_usecase = TaskUsecase(task_repository, assign_repository)
    task_usecase.assign(task_id,user_id)

    message = {"message": "success"}
    return message

@app.get("/tasks/undone")
def get_tasks_undone():
    task_repository = TaskRepository()
    assign_repository = AssignRepository()
    task_usecase = TaskUsecase(task_repository, assign_repository)
    tasks = task_usecase.get_all_tasks_undone()

    response={
        "tasks":tasks
    }
    return response

@app.get("/tasks/noassign")
def get_tasks_noassing():
    task_repository = TaskRepository()
    assign_repository = AssignRepository()
    task_usecase = TaskUsecase(task_repository, assign_repository)
    tasks = task_usecase.get_all_tasks_with_noassign()

    response={
        "tasks":tasks
    }
    return response

@app.get("/tokei/users")
def get_tokei_users():
    user_repository = UserRepository()
    user_usecase = UserUsecase(user_repository)
    users = user_usecase.get_task_count()

    response={
        "users":users
    }
    return response

@app.get("/tokei/rank")
def get_tokei_rank():
    user_repository = UserRepository()
    user_usecase = UserUsecase(user_repository)
    users = user_usecase.user_rank()

    response={
        "users":users
    }
    return response
