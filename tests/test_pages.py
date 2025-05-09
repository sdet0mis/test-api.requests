import allure
from pydantic import BaseModel

from services.pages.pages import PagesService
from services.pages.models import PageModel
from helpers.db import DBConnector


@allure.epic("API")
@allure.feature("Страницы")
@allure.severity(allure.severity_level.BLOCKER)
class TestPages:
    @allure.title("Создание страницы")
    def test_create_page(
        self, db: DBConnector, pages_service: PagesService
    ):
        created_page = pages_service.create_page()
        received_page = db.get_page_by_id(created_page.model.id)
        assert (
            created_page.payloads.title == received_page[0][0]
        ), f"Значения поля 'title' не совпадают, \
            {created_page.payloads.title} != {received_page[0][0]}"
        pages_service.delete_page(created_page.model.id)

    @allure.title("Получение страницы")
    def test_get_page(
        self,
        create_page_by_db: BaseModel,
        pages_service: PagesService
    ):
        received_page = pages_service.get_page(
            create_page_by_db().id
        )
        assert (
            create_page_by_db.title == received_page.model.title.rendered
        ), f"Значения поля 'title' не совпадают, \
            {create_page_by_db.title} != {received_page.model.title.rendered}"

    @allure.title("Изменение страницы")
    def test_update_page(
        self,
        db: DBConnector,
        pages_service: PagesService,
        delete_page: PageModel
    ):
        updated_page = pages_service.update_page(delete_page.model.id)
        received_page = db.get_page_by_id(delete_page.model.id)
        assert (
            updated_page.payloads.title == received_page[0][0]
        ), f"Значения поля 'title' не совпадают, \
            {updated_page.payloads.title} != {received_page[0][0]}"

    @allure.title("Удаление страницы")
    def test_delete_page(
        self,
        db: DBConnector,
        pages_service: PagesService,
        create_page: PageModel
    ):
        deleted_page = pages_service.delete_page(create_page.model.id)
        received_page = db.get_page_by_id(create_page.model.id)
        assert (
            deleted_page.model.deleted is True and received_page == []
        ), f"Страница не удалена, page = {received_page}"
