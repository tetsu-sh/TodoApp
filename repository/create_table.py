
from settings import SQLITE3_NAME
import db
from user_repository import *
import os
 
 
if __name__ == "__main__":
    path = SQLITE3_NAME
    # if not os.path.isfile(path):
 
    # テーブルを作成する
    Base.metadata.create_all(db.engine)
 
