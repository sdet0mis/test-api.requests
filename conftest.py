from typing import Generator

import pytest

from helpers.db import DBConnector
from services.users.users import UsersService
from services.pages.pages import PagesService
from services.posts.posts import PostsService
from services.comments.comments import CommentsService


@pytest.fixture(scope="session", autouse=True)
def db() -> Generator[DBConnector]:
    db = DBConnector()
    yield db
    db.disconnect()


@pytest.fixture()
def users_service() -> UsersService:
    users_service = UsersService()
    return users_service


@pytest.fixture()
def pages_service() -> PagesService:
    pages_service = PagesService()
    return pages_service


@pytest.fixture()
def posts_service() -> PostsService:
    posts_service = PostsService()
    return posts_service


@pytest.fixture()
def comments_service() -> CommentsService:
    comments_service = CommentsService()
    return comments_service
