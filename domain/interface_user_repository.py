from abc import ABCMeta, abstractclassmethod
from domain.user_domain import User

class IUserRepository(metaclass = ABCMeta):
    @abstractclassmethod
    def create(self, user:User):
        pass

    def load(self):
        pass

    def find(self, user_id):
        pass

    def delete(self, user_id):
        pass
