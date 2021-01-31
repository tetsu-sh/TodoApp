from sqlalchemy.sql.sqltypes import Integer
from domain.interface_assign_repository import IAssignRepository
from domain.assign_domain import Assign

from infra.sqlite3.db import Base
import infra.sqlite3.db as db
from infra.sqlite3.task_repository import Task
from infra.sqlite3.user_repository import User

import enum
from sqlalchemy import Column, String, DateTime, ForeignKey, Enum
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.dialects.mysql import INTEGER, BOOLEAN
from sqlalchemy.schema import ForeignKey
from sqlalchemy_utils import UUIDType
from infra.sqlite3.settings import SQLITE3_NAME

import hashlib


class AssignRepository(IAssignRepository):
    def __init__(self):
        pass

    def create(self, assign:Assign):
        print(assign)
        new_assign = Assign(
            assign_id = assign.assign_id,
            task_id = assign.task_id,
            user_id = assign.user_id
            )
        db.session.add(new_assign)
        db.session.commit()
        db.session.close()
        return
    
    def load(self):
        assigns = db.session.query(Assign).all()
        db.session.close()
        print(assigns)
        return assigns
    
    def update_status(self,assign_id,status):
        print(assign_id)
        print(status)
        target_assign = db.session.query(Assign).filter(Assign.assign_id==assign_id)
        target_assign.status = status
        db.session.commit()
        db.session.close()
        return

    def find(self):
        pass

    def delete(self, assign_id):
        db.session.query(Assign).filter(Assign.assign_id==assign_id).delete()
        db.session.commit()
        db.session.close()
        return




class Assign(Base):
    """
    Assignテーブル
 
    assign_id       : 主キー
    task_id         : 外部キー
    user_id         : 外部キー

    """
    __tablename__ = 'assign'
    assign_id = Column(
        'assign_id',
        UUIDType(binary=False),
        primary_key=True,
        # autoincrement=True,
    )
    user_id = Column('user_id', UUIDType(binary=False),ForeignKey("user.user_id"))
    task_id = Column('task_id', UUIDType(binary=False),ForeignKey("task.task_id"))
 
    def __init__(self, assign_id,task_id,user_id):
        self.assign_id = assign_id
        self.task_id = task_id
        self.user_id  =user_id


    def __str__(self):
        return str(self.task_id) + ':' + self.task_name



