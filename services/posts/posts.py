from dataclasses import asdict
from typing import Any

import allure

from helpers.checkers import Checkers
from services.api_client import ApiClient
from services.posts.payloads import PostPayloads
from services.posts.models import PostModel, DeletedPostModel


class PostsService(ApiClient):
    @allure.step("Создать статью")
    def create_post(
        self, expected_code: int = 201, **kwargs
    ) -> dict[str, dict[str, Any] | PostModel]:
        payloads = asdict(PostPayloads(**kwargs))
        self.response = self.post(
            endpoint="/posts", expected_code=expected_code, json=payloads
        )
        if expected_code == 201:
            model = Checkers.validate(PostModel, self.response.json())
            return {"payloads": payloads, "model": model}

    @allure.step("Изменить статью")
    def update_post(
        self, pid: int, expected_code: int = 200, **kwargs
    ) -> dict[str, dict[str, Any] | PostModel]:
        payloads = asdict(PostPayloads(**kwargs))
        self.response = self.post(
            endpoint=f"/posts/{pid}",
            expected_code=expected_code,
            json=payloads
        )
        if expected_code == 200:
            model = Checkers.validate(PostModel, self.response.json())
            return {"payloads": payloads, "model": model}

    @allure.step("Удалить статью")
    def delete_post(
        self, pid: int, expected_code: int = 200
    ) -> DeletedPostModel:
        self.response = self.delete(
            endpoint=f"/posts/{pid}",
            expected_code=expected_code,
            params={"reassign": "", "force": "true"}
        )
        if expected_code == 200:
            return Checkers.validate(DeletedPostModel, self.response.json())
