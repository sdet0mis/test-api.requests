import allure

from helpers.service_data import ServiceDataModel
from services.api_client import ApiClient
from services.posts.payloads import PostPayloads
from services.posts.models import PostModel, DeletedPostModel


class PostsService(ApiClient):
    @allure.step("Создать статью")
    def create_post(
        self,
        expected_code: int = 201,
        validate: bool = True,
        **kwargs: dict
    ) -> ServiceDataModel:
        self.payloads = PostPayloads(**kwargs)
        return self.post(
            endpoint="/posts",
            expected_code=expected_code,
            validate=validate,
            model=PostModel
        )

    @allure.step("Получить статью")
    def get_post(
        self, pid: int, expected_code: int = 200, validate: bool = True
    ) -> ServiceDataModel:
        return self.get(
            endpoint=f"/posts/{pid}",
            expected_code=expected_code,
            validate=validate,
            model=PostModel
        )

    @allure.step("Изменить статью")
    def update_post(
        self,
        pid: int,
        expected_code: int = 200,
        validate: bool = True,
        **kwargs: dict
    ) -> ServiceDataModel:
        self.payloads = PostPayloads(**kwargs)
        return self.post(
            endpoint=f"/posts/{pid}",
            expected_code=expected_code,
            validate=validate,
            model=PostModel
        )

    @allure.step("Удалить статью")
    def delete_post(
        self,
        pid: int,
        expected_code: int = 200,
        validate: bool = True
    ) -> ServiceDataModel:
        return self.delete(
            endpoint=f"/posts/{pid}",
            expected_code=expected_code,
            validate=validate,
            model=DeletedPostModel,
            params={"reassign": "", "force": "true"}
        )
