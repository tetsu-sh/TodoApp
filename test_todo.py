import unittest
from usecase.user_usecase import UserUsecase
from domain.user_domain import User
from infra.inmemory.inmemory_user_repository import InmemoryUserRepository

class TestTodo(unittest.TestCase):


    def test_create_user(self):
        user_repository = InmemoryUserRepository()
        user_usecase = UserUsecase(user_repository)
        mock_user_name = "mock_user"
        user_usecase.create_user(mock_user_name)
    
    def test_get_all_users(self):
        user_repository = InmemoryUserRepository()
        user_usecase = UserUsecase(user_repository)