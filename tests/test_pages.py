import allure

from services.pages.pages import PagesService
from helpers.db import DBConnector


@allure.epic("API")
@allure.feature("Страницы")
@allure.severity(allure.severity_level.BLOCKER)
class TestPages:

    @allure.title("Создание страницы")
    def test_create_page(
        self, db: DBConnector, pages_service: PagesService
    ) -> None:
        created_page = pages_service.create_page()
        received_page = db.get_page_by_id(created_page["model"].id)
        assert created_page["payloads"]["title"] == received_page[0][0]
        pages_service.delete_page(created_page["model"].id)

    @allure.title("Изменение страницы")
    def test_update_page(
        self, db: DBConnector, pages_service: PagesService
    ) -> None:
        created_page = pages_service.create_page()
        updated_page = pages_service.update_page(created_page["model"].id)
        received_page = db.get_page_by_id(created_page["model"].id)
        assert updated_page["payloads"]["title"] == received_page[0][0]
        pages_service.delete_page(created_page["model"].id)

    @allure.title("Удаление страницы")
    def test_delete_page(
        self, db: DBConnector, pages_service: PagesService
    ) -> None:
        created_page = pages_service.create_page()
        deleted_page = pages_service.delete_page(created_page["model"].id)
        received_page = db.get_page_by_id(created_page["model"].id)
        assert deleted_page.deleted is True and received_page == []
