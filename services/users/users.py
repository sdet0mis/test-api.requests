import allure

from helpers.service_data import ServiceDataModel
from services.api_client import ApiClient
from services.users.payloads import CreateUserPayloads, UpdateUserPayloads
from services.users.models import UserModel, DeletedUserModel


class UsersService(ApiClient):
    @allure.step("Создать пользователя")
    def create_user(
        self,
        expected_code: int = 201,
        validate: bool = True,
        **kwargs: dict
    ) -> ServiceDataModel:
        self.payloads = CreateUserPayloads(**kwargs)
        return self.post(
            endpoint="/users",
            expected_code=expected_code,
            validate=validate,
            model=UserModel
        )

    @allure.step("Изменить пользователя")
    def update_user(
        self,
        uid: int,
        expected_code: int = 200,
        validate: bool = True,
        **kwargs: dict
    ) -> ServiceDataModel:
        self.payloads = UpdateUserPayloads(**kwargs)
        return self.post(
            endpoint=f"/users/{uid}",
            expected_code=expected_code,
            validate=validate,
            model=UserModel
        )

    @allure.step("Удалить пользователя")
    def delete_user(
        self,
        uid: int,
        expected_code: int = 200,
        validate: bool = True
    ) -> ServiceDataModel:
        return self.delete(
            endpoint=f"/users/{uid}",
            expected_code=expected_code,
            validate=validate,
            model=DeletedUserModel,
            params={"reassign": "", "force": "true"}
        )
