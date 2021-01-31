from sqlalchemy.sql.sqltypes import Integer
from domain.interface_task_repository import ITaskRepository
from domain.task_domain import Task, Status, Priority

from infra.sqlite3.db import Base
import infra.sqlite3.db as db
from infra.sqlite3.user_repository import User
from infra.sqlite3.assign_repository import Assign

import enum
from sqlalchemy import Column, String, DateTime, ForeignKey, Enum, desc
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.dialects.mysql import INTEGER, BOOLEAN
from sqlalchemy_utils import UUIDType

from infra.sqlite3.settings import SQLITE3_NAME

import hashlib


from logging import getLogger
from common.logger import get_logger


logger = getLogger(__name__)
logger = get_logger(logger)


class TaskRepository(ITaskRepository):
    def __init__(self):
        pass

    def create(self, task:Task):
        print(task)
        new_task = Task(
            task_name = task.task_name,
            task_id = task.task_id,
            status = task.status,
            priority=task.priority,
            description=task.description,
            due_date=task.due_date
            )
        db.session.add(new_task)
        db.session.commit()
        db.session.close()
        return
    
    def load(self):
        tasks = db.session.query(Task).all()
        db.session.close()
        logger.info(tasks)
        return tasks
    
    def update_status(self,task_id,status):
        print(task_id)
        print(status)
        target_task = db.session.query(Task).filter(Task.task_id==task_id)
        target_task.status = status
        db.session.commit()
        db.session.close()
        return

    def find(self):
        pass

    def delete(self, task_id):
        db.session.query(Task).filter(Task.task_id==task_id).delete()
        db.session.commit()
        db.session.close()
        return

class TaskQuery():
    def __init__(self) -> None:
        pass
    
    def query_tasks_status_undone(self):
        tasks = db.session.query(Task).filter(Task.status!=Status(2)).order_by(desc(Task.status)).order_by(desc(Task.priority)).all()
        logger.info(tasks)
        return tasks

    def query_tasks_with_noassign(self):
        tasks = db.session.query(Task, Assign).filter(Task.status!=Status(2)).filter(Task.task_id!=Assign.task_id).order_by(desc(Task.status)).order_by(desc(Task.priority)).join(Assign,Task.task_id==Assign.task_id).all()
        return tasks


class Task(Base):
    """
    Taskテーブル
 
    task_id       : 主キー
    task_name : タスク名
    status : ステータス 0:未着手, 1:着手中,2:完了
    priority : 優先度 0:低,1:中,2:高
    description : 詳細
    due_date : 期日
    """
    __tablename__ = 'task'
    task_id = Column(
        'task_id',
        UUIDType(binary=False),
        primary_key=True,
        # autoincrement=True,
    )
    task_name = Column('task_name', String(256))
    status = Column('status', Enum(Status))
    priority = Column('priority', Enum(Priority))
    description = Column('description', String(256))
    due_date = Column('due_date', DateTime)
 
    def __init__(self, task_id,task_name, status, priority,description, due_date):
        self.task_id = task_id
        self.task_name = task_name
        self.status  =status
        self.priority = priority
        self.descriptin = description
        self.due_date = due_date


    def __str__(self):
        return str(self.task_id) + ':' + self.task_name



