import allure

from helpers.service_data import ServiceDataModel
from services.api_client import ApiClient
from services.pages.payloads import PagePayloads
from services.pages.models import PageModel, DeletedPageModel


class PagesService(ApiClient):
    @allure.step("Создать страницу")
    def create_page(
        self, expected_code: int = 201, validate: bool = True, **kwargs: dict
    ) -> ServiceDataModel:
        self.payloads = PagePayloads(**kwargs)
        return self.post(
            endpoint="/pages",
            expected_code=expected_code,
            validate=validate,
            model=PageModel
        )

    @allure.step("Изменить страницу")
    def update_page(
        self,
        pid: int,
        expected_code: int = 200,
        validate: bool = True,
        **kwargs: dict
    ) -> ServiceDataModel:
        self.payloads = PagePayloads(**kwargs)
        return self.post(
            endpoint=f"/pages/{pid}",
            expected_code=expected_code,
            validate=validate,
            model=PageModel
        )

    @allure.step("Удалить страницу")
    def delete_page(
        self, pid: int, expected_code: int = 200, validate: bool = True,
    ) -> ServiceDataModel:
        return self.delete(
            endpoint=f"/pages/{pid}",
            expected_code=expected_code,
            validate=validate,
            model=DeletedPageModel,
            params={"reassign": "", "force": "true"}
        )
