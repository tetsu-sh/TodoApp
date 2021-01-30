
from infra.sqlite3.settings import SQLITE3_NAME
import infra.sqlite3.db as db
from infra.sqlite3.user_repository import *
import os
 
 
if __name__ == "__main__":
    path = SQLITE3_NAME
    # if not os.path.isfile(path):
 
    # テーブルを作成する
    Base.metadata.create_all(db.engine)
 
