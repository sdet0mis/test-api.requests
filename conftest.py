from typing import Generator

import pytest
from pydantic import BaseModel

from helpers.db import DBConnector
from services.users.users import UsersService
from services.pages.pages import PagesService
from services.posts.posts import PostsService
from services.comments.comments import CommentsService
from services.users.models import UserModel
from services.pages.models import PageModel
from services.posts.models import PostModel
from services.comments.models import CommentModel


@pytest.fixture(scope="session", autouse=True)
def db() -> Generator[DBConnector]:
    db = DBConnector()
    yield db
    db.disconnect()


# users


@pytest.fixture()
def users_service() -> UsersService:
    users_service = UsersService()
    return users_service


@pytest.fixture()
def create_user(users_service: UsersService) -> UserModel:
    return users_service.create_user()


@pytest.fixture()
def delete_user(
    users_service: UsersService, create_user: UserModel
) -> Generator[UserModel]:
    yield create_user
    users_service.delete_user(create_user.model.id)


@pytest.fixture()
def create_user_by_db(db: DBConnector) -> BaseModel:
    user = db.create_user()
    yield user
    db.delete_user(user.id)


# pages


@pytest.fixture()
def pages_service() -> PagesService:
    pages_service = PagesService()
    return pages_service


@pytest.fixture()
def create_page(pages_service: PagesService) -> PageModel:
    return pages_service.create_page()


@pytest.fixture()
def delete_page(
    pages_service: PagesService, create_page: PageModel
) -> Generator[PageModel]:
    yield create_page
    pages_service.delete_page(create_page.model.id)


@pytest.fixture()
def create_page_by_db(db: DBConnector) -> BaseModel:
    page = db.create_page()
    yield page
    db.delete_page(page.id)


# posts


@pytest.fixture()
def posts_service() -> PostsService:
    posts_service = PostsService()
    return posts_service


@pytest.fixture()
def create_post(posts_service: PostsService) -> PostModel:
    return posts_service.create_post()


@pytest.fixture()
def delete_post(
    posts_service: PostsService, create_post: PostModel
) -> Generator[PostModel]:
    yield create_post
    posts_service.delete_post(create_post.model.id)


@pytest.fixture()
def create_post_by_db(db: DBConnector) -> BaseModel:
    post = db.create_post()
    yield post
    db.delete_post(post.id)


# comments


@pytest.fixture()
def comments_service() -> CommentsService:
    comments_service = CommentsService()
    return comments_service


@pytest.fixture()
def create_comment(
    comments_service: CommentsService, delete_post: PostModel
) -> CommentModel:
    return comments_service.create_comment(delete_post.model.id)


@pytest.fixture()
def delete_comment(
    comments_service: CommentsService, create_comment: CommentModel
) -> Generator[CommentModel]:
    yield create_comment
    comments_service.delete_comment(create_comment.model.id)


@pytest.fixture()
def create_comment_by_db(db: DBConnector) -> BaseModel:
    comment = db.create_comment()
    yield comment
    db.delete_comment(comment.id)
