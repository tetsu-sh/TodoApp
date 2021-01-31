from domain.interface_user_repository import IUserRepository
from domain.user_domain import User

from infra.sqlite3.db import Base
import infra.sqlite3.db as db
from infra.sqlite3.task_repository import Task, Status
from infra.sqlite3.assign_repository import Assign

from sqlalchemy import Column, String, DateTime, ForeignKey,desc
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.dialects.mysql import INTEGER, BOOLEAN
from sqlalchemy_utils import UUIDType
from infra.sqlite3.settings import SQLITE3_NAME

import hashlib


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
        print(users)
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
        return tasks
        
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



