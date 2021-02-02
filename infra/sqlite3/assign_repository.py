from sqlalchemy.sql.sqltypes import Integer
from domain.interface_assign_repository import IAssignRepository
from domain.assign_domain import Assign

from infra.sqlite3.db import Base
import infra.sqlite3.db as db
from infra.sqlite3.task_repository import Task
from infra.sqlite3.user_repository import User

import enum
from sqlalchemy import Column, String, DateTime, ForeignKey, Enum
from sqlalchemy.dialects.mysql import INTEGER, BOOLEAN
from sqlalchemy.schema import ForeignKey
from sqlalchemy_utils import UUIDType

from logging import getLogger
from common.logger import get_logger


logger = getLogger(__name__)
logger = get_logger(logger)

class AssignRepository(IAssignRepository):
    def __init__(self):
        pass

    def create(self, assign:Assign):
        new_assign = Assign(
            assign_id = assign.assign_id,
            task_id = assign.task_id,
            user_id = assign.user_id
            )
        session = db.session
        try:
            session.add(new_assign)
            session.commit()
            session.close()
            return
        except Exception as e:
            session.close()
            logger.exception(str(e))
    
    def load(self):
        session = db.session
        try:
            assigns = session.query(Assign).all()
            session.close()
            return assigns
        except Exception as e:
            session.close()
            logger.exception(str(e))


    def update_status(self,assign_id,status):
        session = db.session
        try:
            target_assign = session.query(Assign).filter(Assign.assign_id==assign_id)
            target_assign.status = status
            session.commit()
            session.close()
            return
        except Exception as e:
            session.close()
            logger.exception(str(e))

    def delete(self, assign_id):
        session = db.session
        try:
            session.query(Assign).filter(Assign.assign_id==assign_id).delete()
            session.commit()
            session.close()
            return
        except Exception as e:
            session.close()
            logger.exception(str(e))



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



