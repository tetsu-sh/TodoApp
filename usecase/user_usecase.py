from domain.user_domain import User
import uuid
from domain.interface_user_repository import IUserRepository

class UserUsecase:
    def __init__(self, user_repository: IUserRepository) -> None:
        self.user_repository = user_repository

    def create_user(self,user_name):
        user_id = uuid.uuid4()
        user = User(user_id = user_id, user_name = user_name)
        self.user_repository.create(user)
        return

