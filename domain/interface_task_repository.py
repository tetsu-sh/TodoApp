from abc import ABCMeta, abstractclassmethod
from domain.task_domain import Task

class ITaskRepository(metaclass = ABCMeta):
    @abstractclassmethod
    def create(self, task:Task):
        pass
    @abstractclassmethod
    def load(self):
        pass
    @abstractclassmethod
    def find(self, task_id):
        pass

    @abstractclassmethod
    def delete(self, task_id):
        pass