from domain.interface_user_repository import IUserRepository
from domain.user_domain import User

from infra.sqlite3.db import Base
import infra.sqlite3.db as db
from infra.sqlite3.task_repository import Task, Status,Priority
from infra.sqlite3.assign_repository import Assign

from sqlalchemy import Column, String, DateTime, ForeignKey,desc,func
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.dialects.mysql import INTEGER, BOOLEAN
from sqlalchemy_utils import UUIDType

import hashlib

from logging import getLogger
from common.logger import get_logger


logger = getLogger(__name__)
logger = get_logger(logger)

class UserRepository(IUserRepository):
    def __init__(self):
        pass

    def create(self, user:User):
        new_user = User(user_name = user.user_name,user_id = user.user_id)
        db.session.add(new_user)
        db.session.commit()
        db.session.close()
        return
    
    def load(self):
        users = db.session.query(User).all()
        db.session.close()
        return users

    def find(self):
        pass

    def delete(self, user_id):
        db.session.query(User).filter(User.user_id==user_id).delete()
        db.session.commit()
        db.session.close()
        return


class UserQuery:
    def __init__(self):
        pass

    def query_user_task(self, user_id):
        tasks = db.session.query(Task,Assign).filter(Assign.user_id==user_id).filter(Assign.task_id==Task.task_id).filter(Task.status!=Status(2)).order_by(desc(Task.status)).order_by(desc(Task.priority)).join(Assign,Task.task_id==Assign.task_id).all()
        db.session.close()
        return tasks
    
    def count_wip_task_on_user(self):
        users = db.session.query(User).all()
        user_list = []
        for user in users:
            task_dict = {}
            for p in Priority:
                task_dict[p.value]=db.session.query(Task,User,Assign).filter(Task.priority==p).filter(Assign.user_id==user.user_id).filter(Assign.task_id==Task.task_id).filter(Task.status==Status(1)).count()
            user_list.append({"user_id":user.user_id,"task_count":task_dict})
        db.session.close()
        return user_list

    def count_done_on_user(self):
        users = db.session.query(User).all()
        user_list = []
        for user in users:
            tasks = db.session.query(Task,Assign).filter(Assign.user_id==user.user_id).filter(Assign.task_id==Task.task_id).filter(Task.status==Status(2)).count()
            user_list.append({"user_id":user.user_id,"count":tasks})
        user_list = sorted(user_list,key=lambda x:x["count"])
        db.session.close()
        return user_list

class User(Base):
    """
    Userテーブル
 
    user_id       : 主キー
    user_name : ユーザネーム
    """
    __tablename__ = 'user'
    user_id = Column(
        'user_id',
        UUIDType(binary=False),
        primary_key=True,
        # autoincrement=True,
    )
    user_name = Column('user_name', String(256))
 
    def __init__(self, user_id,user_name):
        self.user_id = user_id
        self.user_name = user_name
 
    def __str__(self):
        return str(self.user_id) + ':' + self.user_name



