from usecase.user_usecase import UserUsecase
from infra.sqlite3.user_repository import UserRepository
from logging import getLogger
from common.logger import get_logger
logger = getLogger(__name__)
logger = get_logger(logger)

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


app = FastAPI()


class User(BaseModel):
    user_name: str

    class Config:
        schema_extra = {
            "example":{
                "user_name":"test_user"
            }

        }

@app.post("/user")
def create_user(user: User):
    logger.info("start create user")


    user_repository = UserRepository()
    user_usecase = UserUsecase(user_repository)
    user_usecase.create_user(user.user_name)

    message = {"message": "success"}
    return message


@app.get("/users")
def get_all_users():
    user_repository = UserRepository()
    user_usecase = UserUsecase(user_repository)
    users = user_usecase.get_all_users()
    response={
        "users":users
    }
    return response

@app.delete("/user/{user_id}")
def delete_user(user_id):
    user_repository = UserRepository()
    user_usecase = UserUsecase(user_repository)
    user_usecase.delete_user(user_id)

    message = {"message": "success"}
    return message