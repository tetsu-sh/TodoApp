from domain.interface_assign_repository import IAssignRepository
from domain.assign_domain import Assign
import uuid

class InmemoryAssignRepository(IAssignRepository):
    def __init__(self):
        self.data = []

    def create(self, assign:Assign):
        new_assign = {
            "assign_id" :assign.assign_id,
            "task_id":assign.task_id,
            "user_id":assign.user_id
        }
        self.data.append(new_assign)
        return

    def load(self):
        return self.data

    def find(self, assign_id):
        res = [k for k ,v in self.data.items() if v==assign_id]

        return res

    def delete(self, assign_id):
        pass