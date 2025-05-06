import allure

from services.users.users import UsersService
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
        received_user = db.get_user_by_id(created_user["model"].id)
        assert created_user["payloads"]["username"] == received_user[0][0] \
            and created_user["payloads"]["email"] == received_user[0][1]
        users_service.delete_user(created_user["model"].id)

    @allure.title("Изменение пользователя")
    def test_update_user(
        self, db: DBConnector, users_service: UsersService
    ):
        created_user = users_service.create_user()
        updated_user = users_service.update_user(created_user["model"].id)
        received_user = db.get_user_by_id(created_user["model"].id)
        assert updated_user["payloads"]["email"] == received_user[0][1]
        users_service.delete_user(created_user["model"].id)

    @allure.title("Удаление пользователя")
    def test_delete_user(
        self, db: DBConnector, users_service: UsersService
    ):
        created_user = users_service.create_user()
        deleted_user = users_service.delete_user(created_user["model"].id)
        received_user = db.get_user_by_id(created_user["model"].id)
        assert deleted_user.deleted is True and received_user == []
