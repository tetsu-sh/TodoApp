from domain.interface_user_repository import IUserRepository
# from domain.user import User

from infrastructure.sqlite3.db import Base
import infrastructure.sqlite3.db as db

from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.dialects.mysql import INTEGER, BOOLEAN
from infrastructure.sqlite3.settings import SQLITE3_NAME

import hashlib


class UserRepository(IUserRepository):
    def __init__(self):
        pass

    def create(self, User):
        new_user = UserModel(username = User.user_name)
        db.session.add(new_user)
        db.session.commit()
        db.session.close()
    
    def load(self):
        pass

    def find(self):
        pass


class UserModel(Base):
    """
    Userテーブル
 
    id       : 主キー
    username : ユーザネーム
    """
    __tablename__ = 'user'
    user_id = Column(
        'user_id',
        INTEGER(unsigned=True),
        primary_key=True,
        autoincrement=True,
    )
    user_name = Column('user_name', String(256))
 
    def __init__(self, username):
        self.username = username
        # パスワードはハッシュ化して保存
 
    def __str__(self):
        return str(self.id) + ':' + self.username

def main():
    user_repository = UserRepository()
    user_repository.create(user_name="test_user")

