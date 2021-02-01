import unittest
import os
# from usecase.user_usecase import UserUsecase
# from domain.user_domain import User
# from infra.inmemory.inmemory_user_repository import InmemoryUserRepository

from presentation.server import app
from fastapi.testclient import TestClient
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from infra.sqlite3.db import Base

# client = TestClient(app)

# RDB_PATH = 'sqlite:///infra/sqlite3/test_db.sqlite3'
# os.environ["RDB_PATH"] = RDB_PATH

# SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )
# TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base.metadata.create_all(bind=engine)


# def override_get_db():
#     try:
#         db = TestingSessionLocal()
#         yield db
#     finally:
#         db.close()

# app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_get_all_user():
    response = client.get("/users")
    print(response)

# class TestTodo(unittest.TestCase):

#     def setUp(self) -> None:
#         self.inmemory_user_repository=InmemoryUserRepository()

#     def test_create_user(self):
#         user_usecase = UserUsecase(self.inmemory_user_repository)
#         mock_user_name = "mock_user"
#         user_usecase.create_user(mock_user_name)
    
#     def test_get_all_users(self):
#         user_usecase = UserUsecase(self.inmemory_user_repository)
#         users = user_usecase.get_all_users()
#         assert users[0]["user_name"]=="mock_user"