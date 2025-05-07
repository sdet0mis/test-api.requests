import allure

from services.posts.posts import PostsService
from services.comments.comments import CommentsService
from services.comments.models import CommentModel
from helpers.db import DBConnector


@allure.epic("API")
@allure.feature("Комментарии")
@allure.severity(allure.severity_level.BLOCKER)
class TestComments:
    @allure.title("Создание комментария")
    def test_create_comment(
        self,
        db: DBConnector,
        posts_service: PostsService,
        comments_service: CommentsService
    ):
        created_post = posts_service.create_post()
        created_comment = comments_service.create_comment(
            created_post.model.id
        )
        received_comment = db.get_comment_by_id(created_comment.model.id)
        assert (
            created_comment.payloads.content == received_comment[0][0]
        ), f"Значения поля 'content' не совпадают, \
            {created_comment.payloads.content} != {received_comment[0][0]}"
        posts_service.delete_post(created_post.model.id)

    @allure.title("Изменение комментария")
    def test_update_comment(
        self,
        db: DBConnector,
        comments_service: CommentsService,
        delete_comment: CommentModel
    ):
        updated_comment = comments_service.update_comment(
            delete_comment.model.id
        )
        received_comment = db.get_comment_by_id(delete_comment.model.id)
        assert (
            updated_comment.payloads.content == received_comment[0][0]
        ), f"Значения поля 'content' не совпадают, \
            {updated_comment.payloads.content} != {received_comment[0][0]}"

    @allure.title("Удаление комментария")
    def test_delete_comment(
        self,
        db: DBConnector,
        comments_service: CommentsService,
        create_comment: CommentModel
    ):
        deleted_comment = comments_service.delete_comment(
            create_comment.model.id
        )
        received_comment = db.get_comment_by_id(create_comment.model.id)
        assert (
            deleted_comment.model.deleted is True and received_comment == []
        ), f"Комментарий не удален, comment = {received_comment}"
