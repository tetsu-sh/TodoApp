from abc import ABCMeta, abstractclassmethod
from domain.assign_domain import Assign

class IAssignRepository(metaclass = ABCMeta):
    @abstractclassmethod
    def create(self, assign:Assign):
        pass

    def load(self):
        pass

    def find(self, user_id):
        pass

    def delete(self, user_id):
        pass