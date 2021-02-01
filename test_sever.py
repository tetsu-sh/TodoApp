import unittest
import os
from usecase.user_usecase import UserUsecase
from domain.user_domain import User
from infra.inmemory.inmemory_user_repository import InmemoryUserRepository
from usecase.task_usecase import TaskUsecase
from domain.task_domain import Task, Status, Priority
from infra.inmemory.inmemory_task_repository import InmemoryTaskRepository
from domain.assign_domain import Assign
from infra.inmemory.inmemory_assign_repository import InmemoryAssignRepository

from presentation.server import app
from fastapi.testclient import TestClient


class TestTodo(unittest.TestCase):

    def setUp(self) -> None:
        print("start")
        self.inmemory_user_repository=InmemoryUserRepository()
        self.inmemory_task_repository=InmemoryTaskRepository()
        self.inmemory_assign_repository=InmemoryAssignRepository()

    def test_create_user(self):
        user_usecase = UserUsecase(self.inmemory_user_repository)
        mock_user_name = "mock_user"
        user_usecase.create_user(mock_user_name)
        assert self.inmemory_user_repository.data[0]["user_name"] == mock_user_name
    
    def test_get_all_users(self):
        self.test_create_user()
        user_usecase = UserUsecase(self.inmemory_user_repository)
        users = user_usecase.get_all_users()
        print(users)
        assert users["users"][0]["user_name"]=="mock_user"
    
    def test_create_task(self):
        task_usecase=TaskUsecase(self.inmemory_task_repository,self.inmemory_assign_repository)
        mock_task_name = "mock_task"
        mock_priority = 2
        mock_description = "mock_description"
        mock_due_date = "2021-02-03T21:43:25.814250"
        task_usecase.create_task(mock_task_name,mock_priority, mock_description,mock_due_date)
        assert self.inmemory_task_repository.data[0]["task_name"] == mock_task_name
        assert self.inmemory_task_repository.data[0]["priority"] == Priority(mock_priority)
        assert self.inmemory_task_repository.data[0]["description"] == mock_description
        assert self.inmemory_task_repository.data[0]["due_date"] == mock_due_date
        assert self.inmemory_task_repository.data[0]["status"] == Status(0)

    def test_assign(self):
        self.test_create_user()
        self.test_create_task()
        task_usecase=TaskUsecase(self.inmemory_task_repository,self.inmemory_assign_repository)
        mock_user_id = self.inmemory_user_repository.data[0]["user_id"]
        mock_task_id = self.inmemory_task_repository.data[0]["task_id"]
        task_usecase.assign(mock_task_id,mock_user_id)
        assert self.inmemory_assign_repository.data[0]["task_id"] == mock_task_id
        assert self.inmemory_assign_repository.data[0]["user_id"] == mock_user_id
    
    def test_status_wip(self):
        self.test_assign()
        task_usecase=TaskUsecase(self.inmemory_task_repository,self.inmemory_assign_repository)
        mock_task_id = self.inmemory_task_repository.data[0]["task_id"]
        task_usecase.task_status_wip(mock_task_id)
        assert self.inmemory_task_repository.data[0]["status"] == Status(1)
    
    def test_status_done(self):
        self.test_assign()
        task_usecase=TaskUsecase(self.inmemory_task_repository,self.inmemory_assign_repository)
        mock_task_id = self.inmemory_task_repository.data[0]["task_id"]
        task_usecase.task_status_done(mock_task_id)
        assert self.inmemory_task_repository.data[0]["status"] == Status(2)