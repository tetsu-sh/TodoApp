from domain.interface_user_repository import IUserRepository
# from domain.user import User

from repository.db import Base
import repository.db

from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.dialects.mysql import INTEGER, BOOLEAN
from repository.settings import SQLITE3_NAME

import hashlib


class UserRepository(IUserRepository):
    def __init__(self):
        pass

    def create(self, User):
        new_user = User(username = User.user_name)
        db.session.add(new_user)
        db.session.commit()
        db.session.close()


class User(Base):
    """
    Userテーブル
 
    id       : 主キー
    username : ユーザネーム
    """
    __tablename__ = 'user'
    id = Column(
        'id',
        INTEGER(unsigned=True),
        primary_key=True,
        autoincrement=True,
    )
    username = Column('username', String(256))
 
    def __init__(self, username):
        self.username = username
        # パスワードはハッシュ化して保存
 
    def __str__(self):
        return str(self.id) + ':' + self.username

def main():
    user_repository = UserRepository()
    user_repository.create(user_name="test_user")

