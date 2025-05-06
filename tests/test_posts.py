import allure

from services.posts.posts import PostsService
from helpers.db import DBConnector


@allure.epic("API")
@allure.feature("Статьи")
@allure.severity(allure.severity_level.BLOCKER)
class TestPosts:
    @allure.title("Создание статьи")
    def test_create_post(
        self, db: DBConnector, posts_service: PostsService
    ):
        created_post = posts_service.create_post()
        received_post = db.get_post_by_id(created_post["model"].id)
        assert created_post["payloads"]["title"] == received_post[0][0]
        posts_service.delete_post(created_post["model"].id)

    @allure.title("Изменение статьи")
    def test_update_post(
        self, db: DBConnector, posts_service: PostsService
    ):
        created_post = posts_service.create_post()
        updated_post = posts_service.update_post(created_post["model"].id)
        received_post = db.get_post_by_id(created_post["model"].id)
        assert updated_post["payloads"]["title"] == received_post[0][0]
        posts_service.delete_post(created_post["model"].id)

    @allure.title("Удаление статьи")
    def test_delete_post(
        self, db: DBConnector, posts_service: PostsService
    ):
        created_post = posts_service.create_post()
        deleted_post = posts_service.delete_post(created_post["model"].id)
        received_post = db.get_post_by_id(created_post["model"].id)
        assert deleted_post.deleted is True and received_post == []
