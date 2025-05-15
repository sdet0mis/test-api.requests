from typing import Generator

import pytest
from pydantic import BaseModel

from helpers.db import DBConnector
from services.posts.posts import PostsService
from services.posts.models import PostModel


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
