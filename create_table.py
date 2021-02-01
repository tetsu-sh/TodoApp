
import infra.sqlite3.db as db
from infra.sqlite3.user_repository import Base as BaseUser
from infra.sqlite3.task_repository import Base as BaseTask
from infra.sqlite3.assign_repository import Base as BaseAssign


if __name__ == "__main__":
    
    # テーブルを作成する
    BaseUser.metadata.create_all(db.engine)
    BaseTask.metadata.create_all(db.engine)
    BaseAssign.metadata.create_all(db.engine)

 
