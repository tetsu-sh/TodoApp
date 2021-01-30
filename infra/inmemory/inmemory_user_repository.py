from domain.interface_user_repository import IUserRepository
from domain.user_domain import User

class InmemoryUserRepository(IUserRepository):
    def __init__(self):
        pass

    def create(self, user:User):
        pass

    def load(self):
        pass

    def find(self):
        pass