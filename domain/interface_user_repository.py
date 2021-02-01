from abc import ABCMeta, abstractclassmethod
from domain.user_domain import User

class IUserRepository(metaclass = ABCMeta):
    @abstractclassmethod
    def create(self, user:User):
        pass

    @abstractclassmethod
    def load(self):
        pass

    @abstractclassmethod
    def find(self, user_id):
        pass

    @abstractclassmethod
    def delete(self, user_id):
        pass
