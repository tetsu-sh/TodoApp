from abc import ABCMeta, abstractclassmethod
from domain.assign_domain import Assign

class IAssignRepository(metaclass = ABCMeta):
    @abstractclassmethod
    def create(self, assign:Assign):
        pass

    @abstractclassmethod
    def load(self):
        pass

    @abstractclassmethod
    def find(self, assign_id):
        pass

    @abstractclassmethod
    def delete(self, assign_id):
        pass