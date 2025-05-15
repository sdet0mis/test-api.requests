from typing import Generator

import pytest
from pydantic import BaseModel

from helpers.db import DBConnector
from services.users.users import UsersService
from services.users.models import UserModel


@pytest.fixture()
def users_service() -> UsersService:
    users_service = UsersService()
    return users_service


@pytest.fixture()
def create_user(users_service: UsersService) -> UserModel:
    return users_service.create_user()


@pytest.fixture()
def delete_user(
    users_service: UsersService, create_user: UserModel
) -> Generator[UserModel]:
    yield create_user
    users_service.delete_user(create_user.model.id)


@pytest.fixture()
def create_user_by_db(db: DBConnector) -> BaseModel:
    user = db.create_user()
    yield user
    db.delete_user(user.id)
