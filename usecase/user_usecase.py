from domain.user_domain import User
import uuid
from domain.interface_user_repository import IUserRepository
from infra.sqlite3.user_repository import UserQuery

class UserUsecase:
    def __init__(self, user_repository: IUserRepository) -> None:
        self.user_repository = user_repository

    def create_user(self,user_name):
        user_id = uuid.uuid4()
        user = User(user_id = user_id, user_name = user_name)
        self.user_repository.create(user)
        return
    
    def get_all_users(self):
        users = self.user_repository.load()
        return users
    
    def delete_user(self, user_id):
        self.user_repository.delete(user_id)
        return
        
    def get_user_task(self, user_id):
        query = UserQuery()
        tasks = query.query_user_task(user_id)
        return tasks