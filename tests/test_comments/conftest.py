from typing import Generator

import pytest
from pydantic import BaseModel

from helpers.db import DBConnector
from services.comments.comments import CommentsService
from services.posts.models import PostModel
from services.comments.models import CommentModel
from tests.test_posts.conftest import create_post, delete_post, posts_service


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
