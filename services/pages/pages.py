from dataclasses import asdict
from typing import Any

import allure

from helpers.checkers import Checkers
from services.api_client import ApiClient
from services.pages.payloads import PagePayloads
from services.pages.models import PageModel, DeletedPageModel


class PagesService(ApiClient):

    @allure.step("Создать страницу")
    def create_page(
        self, expected_code: int = 201, **kwargs
    ) -> dict[str, dict[str, Any] | PageModel]:
        payloads = asdict(PagePayloads(**kwargs))
        self.response = self.post(
            endpoint="/pages", expected_code=expected_code, json=payloads
        )
        if expected_code == 201:
            model = Checkers.validate(PageModel, self.response.json())
            return {"payloads": payloads, "model": model}

    @allure.step("Изменить страницу")
    def update_page(
        self, pid: int, expected_code: int = 200, **kwargs
    ) -> dict[str, dict[str, Any] | PageModel]:
        payloads = asdict(PagePayloads(**kwargs))
        self.response = self.post(
            endpoint=f"/pages/{pid}",
            expected_code=expected_code,
            json=payloads
        )
        if expected_code == 200:
            model = Checkers.validate(PageModel, self.response.json())
            return {"payloads": payloads, "model": model}

    @allure.step("Удалить страницу")
    def delete_page(
        self, pid: int, expected_code: int = 200
    ) -> DeletedPageModel:
        self.response = self.delete(
            endpoint=f"/pages/{pid}",
            expected_code=expected_code,
            params={"reassign": "", "force": "true"}
        )
        if expected_code == 200:
            return Checkers.validate(DeletedPageModel, self.response.json())
