import allure

from services.users.users import UsersService
from services.users.models import UserModel
from helpers.db import DBConnector


@allure.epic("API")
@allure.feature("Пользователи")
@allure.severity(allure.severity_level.BLOCKER)
class TestUsers:
    @allure.title("Создание пользователя")
    def test_create_user(
        self, db: DBConnector, users_service: UsersService
    ):
        created_user = users_service.create_user()
        received_user = db.get_user_by_id(created_user.model.id)
        assert (
            created_user.payloads.username == received_user[0][0]
        ), f"Значения поля 'username' не совпадают, \
            {created_user.payloads.username} != {received_user[0][0]}"
        assert (
            created_user.payloads.email == received_user[0][1]
        ), f"Значения поля 'email' не совпадают, \
            {created_user.payloads.email} != {received_user[0][1]}"
        users_service.delete_user(created_user.model.id)

    @allure.title("Изменение пользователя")
    def test_update_user(
        self,
        db: DBConnector,
        users_service: UsersService,
        delete_user: UserModel
    ):
        updated_user = users_service.update_user(delete_user.model.id)
        received_user = db.get_user_by_id(delete_user.model.id)
        assert (
            updated_user.payloads.email == received_user[0][1]
        ), f"Значения поля 'email' не совпадают, \
            {updated_user.payloads.email} != {received_user[0][1]}"

    @allure.title("Удаление пользователя")
    def test_delete_user(
        self,
        db: DBConnector,
        users_service: UsersService,
        create_user: UserModel
    ):
        deleted_user = users_service.delete_user(create_user.model.id)
        received_user = db.get_user_by_id(create_user.model.id)
        assert (
            deleted_user.model.deleted is True and received_user == []
        ), f"Пользователь не удален, user = {received_user}"
