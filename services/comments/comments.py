from dataclasses import asdict
from typing import Any

import allure

from helpers.checkers import Checkers
from services.api_client import ApiClient
from services.comments.models import CommentModel, DeletedCommentModel
from services.comments.payloads import (
    CreateCommentPayloads, UpdateCommentPayloads
)


class CommentsService(ApiClient):

    @allure.step("Создать комментарий")
    def create_comment(
        self, post: int, expected_code: int = 201, **kwargs
    ) -> dict[str, dict[str, Any] | CommentModel]:
        payloads = asdict(CreateCommentPayloads(post=post, **kwargs))
        self.response = self.post(
            endpoint="/comments", expected_code=expected_code, json=payloads
        )
        if expected_code == 201:
            model = Checkers.validate(CommentModel, self.response.json())
            return {"payloads": payloads, "model": model}

    @allure.step("Изменить комментарий")
    def update_comment(
        self, cid: int, expected_code: int = 200, **kwargs
    ) -> dict[str, dict[str, Any] | CommentModel]:
        payloads = asdict(UpdateCommentPayloads(**kwargs))
        self.response = self.post(
            endpoint=f"/comments/{cid}",
            expected_code=expected_code,
            json=payloads
        )
        if expected_code == 200:
            model = Checkers.validate(CommentModel, self.response.json())
            return {"payloads": payloads, "model": model}

    @allure.step("Удалить комментарий")
    def delete_comment(
        self, cid: int, expected_code: int = 200
    ) -> DeletedCommentModel:
        self.response = self.delete(
            endpoint=f"/comments/{cid}",
            expected_code=expected_code,
            params={"reassign": "", "force": "true"}
        )
        if expected_code == 200:
            return Checkers.validate(DeletedCommentModel, self.response.json())
