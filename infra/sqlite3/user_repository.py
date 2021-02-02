from domain.interface_user_repository import IUserRepository
from domain.user_domain import User

from infra.sqlite3.db import Base
import infra.sqlite3.db as db
from infra.sqlite3.task_repository import Task, Status,Priority
from infra.sqlite3.assign_repository import Assign

from sqlalchemy import Column, String, DateTime, ForeignKey,desc
from sqlalchemy.dialects.mysql import INTEGER, BOOLEAN
from sqlalchemy_utils import UUIDType

from logging import getLogger
from common.logger import get_logger


logger = getLogger(__name__)
logger = get_logger(logger)

class UserRepository(IUserRepository):
    def __init__(self):
        pass

    def create(self, user:User):
        new_user = User(user_name = user.user_name,user_id = user.user_id)
        session = db.session
        try:
            session.add(new_user)
            session.commit()
            session.close()
            return
        except Exception as e:
            session.close()
            logger.exception(str(e))
        
    
    def load(self):
        session = db.session
        try:
            users = db.session.query(User).all()
            session.close()
            return users

        except Exception as e:
            session.close()
            logger.exception(str(e))


    def delete(self, user_id):
        session = db.session
        try:
            session.query(User).filter(User.user_id==user_id).delete()
            session.commit()
            session.close()
            return
        except Exception as e:
            session.close()
            logger.exception(str(e))


class UserQuery:
    def __init__(self):
        pass

    def query_user_task(self, user_id):
        session  =db.session
        try:
            tasks = db.session.query(Task).filter(Assign.task_id==Task.task_id).filter(Assign.user_id==user_id).filter(Task.status!=Status("done")).order_by(desc(Task.status),desc(Task.priority)).all()
            db.session.close()
            return tasks
        except Exception as e:
            session.close()
            logger.exception(str(e))
    
    def count_wip_task_on_user(self):
        session = db.session
        try:
            users = session.query(User).all()
            user_list = []
            for user in users:
                task_dict = {}
                for p in Priority:
                    task_dict[p.value]=session.query(Task).filter(Task.priority==p).filter(Assign.user_id==user.user_id).filter(Assign.task_id==Task.task_id).filter(Task.status==Status("wip")).count()
                user_list.append({"user_id":user.user_id,"task_count":task_dict})
            session.close()
            return user_list
        except Exception as e:
            session.close()
            logger.exception(str(e))

    def count_done_on_user(self):
        session = db.session
        try:
            users = session.query(User).all()
            user_list = []
            for user in users:
                tasks = session.query(Task,Assign).filter(Assign.user_id==user.user_id).filter(Assign.task_id==Task.task_id).filter(Task.status==Status("done")).count()
                user_list.append({"user_id":user.user_id,"count":tasks})
            user_list = sorted(user_list,key=lambda x:x["count"])
            session.close()
            return user_list
        except Exception as e:
            session.close()
            logger.exception(str(e))

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



