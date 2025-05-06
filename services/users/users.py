from dataclasses import asdict
from typing import Any

import allure

from helpers.checkers import Checkers
from services.api_client import ApiClient
from services.users.payloads import CreateUserPayloads, UpdateUserPayloads
from services.users.models import UserModel, DeletedUserModel


class UsersService(ApiClient):
    @allure.step("Создать пользователя")
    def create_user(
        self, expected_code: int = 201, **kwargs
    ) -> dict[str, dict[str, Any] | UserModel]:
        payloads = asdict(CreateUserPayloads(**kwargs))
        self.response = self.post(
            endpoint="/users", expected_code=expected_code, json=payloads
        )
        if expected_code == 201:
            model = Checkers.validate(UserModel, self.response.json())
            return {"payloads": payloads, "model": model}

    @allure.step("Изменить пользователя")
    def update_user(
        self, uid: int, expected_code: int = 200, **kwargs
    ) -> dict[str, dict[str, Any] | UserModel]:
        payloads = asdict(UpdateUserPayloads(**kwargs))
        self.response = self.post(
            endpoint=f"/users/{uid}",
            expected_code=expected_code,
            json=payloads
        )
        if expected_code == 200:
            model = Checkers.validate(UserModel, self.response.json())
            return {"payloads": payloads, "model": model}

    @allure.step("Удалить пользователя")
    def delete_user(
        self, uid: int, expected_code: int = 200
    ) -> DeletedUserModel:
        self.response = self.delete(
            endpoint=f"/users/{uid}",
            expected_code=expected_code,
            params={"reassign": "", "force": "true"}
        )
        if expected_code == 200:
            return Checkers.validate(DeletedUserModel, self.response.json())
