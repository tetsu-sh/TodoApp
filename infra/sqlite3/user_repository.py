from domain.interface_user_repository import IUserRepository
from domain.user_domain import User

from infra.sqlite3.db import Base
import infra.sqlite3.db as db

from sqlalchemy import Column, String, DateTime, ForeignKey
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
    
    def load(self):
        users = db.session.query(User).all()
        print(users)
        return users

    def find(self):
        pass


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



