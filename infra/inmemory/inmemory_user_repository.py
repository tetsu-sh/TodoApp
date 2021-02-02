from domain.interface_user_repository import IUserRepository
from domain.user_domain import User
import uuid

class InmemoryUserRepository(IUserRepository):
    def __init__(self):
        self.data = []

    def create(self, user:User):
        new_user = {
            "user_id" :user.user_id,
            "user_name": user.user_name,
        }
        self.data.append(new_user)
        return

    def load(self):
        return {"users":self.data}

    def find(self, user_id):
        f = [k for k ,v in self.data.items() if v==user_id]

        return {"users":[f]}

    def delete(self, user_id):
        pass