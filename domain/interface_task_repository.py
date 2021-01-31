from abc import ABCMeta, abstractclassmethod
from domain.task_domain import Task

class ITaskRepository(metaclass = ABCMeta):
    @abstractclassmethod
    def create(self, task:Task):
        pass

    def load(self):
        pass

    def find(self, user_id):
        pass

    def delete(self, user_id):
        pass