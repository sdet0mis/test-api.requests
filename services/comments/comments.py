import allure

from helpers.service_data import ServiceDataModel
from services.api_client import ApiClient
from services.comments.models import CommentModel, DeletedCommentModel
from services.comments.payloads import (
    CreateCommentPayloads, UpdateCommentPayloads
)


class CommentsService(ApiClient):
    @allure.step("Создать комментарий")
    def create_comment(
        self,
        post: int,
        expected_code: int = 201,
        validate: bool = True,
        **kwargs: dict
    ) -> ServiceDataModel:
        self.payloads = CreateCommentPayloads(post=post, **kwargs)
        return self.post(
            endpoint="/comments",
            expected_code=expected_code,
            validate=validate,
            model=CommentModel
        )

    @allure.step("Получить комментарий")
    def get_page(
        self, cid: int, expected_code: int = 200, validate: bool = True
    ) -> ServiceDataModel:
        return self.get(
            endpoint=f"/comments/{cid}",
            expected_code=expected_code,
            validate=validate,
            model=CommentModel
        )

    @allure.step("Изменить комментарий")
    def update_comment(
        self,
        cid: int,
        expected_code: int = 200,
        validate: bool = True,
        **kwargs: dict
    ) -> ServiceDataModel:
        self.payloads = UpdateCommentPayloads(**kwargs)
        return self.post(
            endpoint=f"/comments/{cid}",
            expected_code=expected_code,
            validate=validate,
            model=CommentModel
        )

    @allure.step("Удалить комментарий")
    def delete_comment(
        self,
        cid: int,
        expected_code: int = 200,
        validate: bool = True,
    ) -> ServiceDataModel:
        return self.delete(
            endpoint=f"/comments/{cid}",
            expected_code=expected_code,
            validate=validate,
            model=DeletedCommentModel,
            params={"reassign": "", "force": "true"}
        )
