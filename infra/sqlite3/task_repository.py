from sqlalchemy.sql.sqltypes import Integer
from domain.interface_task_repository import ITaskRepository
from domain.task_domain import Task, Status, Priority

from infra.sqlite3.db import Base
import infra.sqlite3.db as db
from infra.sqlite3.user_repository import User
from infra.sqlite3.assign_repository import Assign

import enum
from sqlalchemy import Column, String, DateTime, ForeignKey, Enum, desc
from sqlalchemy.dialects.mysql import INTEGER, BOOLEAN
from sqlalchemy_utils import UUIDType

from logging import getLogger
from common.logger import get_logger


logger = getLogger(__name__)
logger = get_logger(logger)


class TaskRepository(ITaskRepository):
    def __init__(self):
        pass

    def create(self, task:Task):
        new_task = Task(
            task_name = task.task_name,
            task_id = task.task_id,
            status = task.status,
            priority=task.priority,
            description=task.description,
            due_date=task.due_date
            )
        session = db.session
        try:
            session.add(new_task)
            session.commit()
            session.close()
            return
        except Exception as e:
            session.close()
            logger.exception(str(e))

    
    def load(self):
        session = db.session
        try:
            tasks = session.query(Task).all()
            session.close()
            logger.info(tasks)
            return tasks
        except Exception as e:
            session.close()
            logger.exception(str(e))
        
    
    def update_status(self,task_id,status):
        logger.info(task_id)
        logger.info(status)
        session = db.session
        try:    
            target_task = session.query(Task).filter(Task.task_id==task_id).first()
            target_task.status = status
            session.commit()
            session.close()
            return
        except Exception as e:
            session.close()
            logger.exception(str(e))


    def delete(self, task_id):
        session=db.session
        try:
            session.query(Task).filter(Task.task_id==task_id).delete()
            session.commit()
            session.close()
            return
        except Exception as e:
            session.close()
            logger.exception(str(e))

class TaskQuery():
    def __init__(self) -> None:
        pass
    
    def query_tasks_status_undone(self):
        session = db.session
        try:
            tasks = session.query(Task).filter(Task.status!=Status("done")).order_by(desc(Task.status),desc(Task.priority)).all()
            logger.info(tasks)
            session.close()
            return tasks
        except Exception as e:
            session.close()
            logger.exception(str(e))

    def query_tasks_with_noassign(self):
        session = db.session
        try:
            # tasks = session.query(Task).filter(Task.status!=Status("done")).filter(Task.task_id!=Assign.task_id).order_by(desc(Task.priority),desc(Task.status)).all()
            tasks = session.query(Task).filter(Task.status!=Status("done")).outerjoin(Assign,Task.task_id==Assign.task_id).filter(Assign.task_id==None).order_by(desc(Task.priority),desc(Task.status)).all()
            
            session.close()
            return tasks
        except Exception as e:
            session.close()
            logger.exception(str(e))

class Task(Base):
    """
    Taskテーブル
 
    task_id       : 主キー
    task_name : タスク名
    status : ステータス a:new(未着手), b:wip(着手中),c:done(完了)
    priority : 優先度 a:low(低),b:middle(中),c:high(高)
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
        self.description = description
        self.due_date = due_date


    def __str__(self):
        return str(self.task_id) + ':' + self.task_name



