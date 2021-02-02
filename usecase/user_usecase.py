from domain.user_domain import User
import uuid
from domain.interface_user_repository import IUserRepository
from infra.sqlite3.user_repository import UserQuery

class UserUsecase:
    def __init__(self, user_repository: IUserRepository) -> None:
        self.user_repository = user_repository

    def create_user(self,user_name):
        """
        ユーザ登録
        """
        user_id = uuid.uuid4()
        user = User(user_id = user_id, user_name = user_name)
        self.user_repository.create(user)
        return
    
    def get_all_users(self):
        """
        ユーザ一覧
        """
        users = self.user_repository.load()
        return users
    
    def delete_user(self, user_id):
        """
        ユーザ削除
        """
        self.user_repository.delete(user_id)
        return
        
    def get_user_task_undone(self, user_id):
        """
        あるユーザが担当している未完了のタスクを一覧表示する。出力順は作業状態(作業中->未着手)及び、同じ作業状態であれば優先度の高い順とする。
        """
        query = UserQuery()
        tasks = query.query_user_tasks_undone(user_id)
        return tasks

    def get_users_wip_count(self):
        """
        ユーザごとのアサインされている作業中タスクの数。優先順位別にカウントして表示する。
        """
        query = UserQuery()
        users = query.count_wip_task_on_user()
        return users
    
    def get_users_done_count(self):
        """
        多くのタスクを完了させたユーザのランキング。（二人以上で担当していた場合には、それぞれのユーザに対してタスク完了数を１つ足すものとする）
        """
        query = UserQuery()
        users = query.count_done_on_user()
        return users