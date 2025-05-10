from typing import Generator

import pytest
from pydantic import BaseModel

from helpers.db import DBConnector
from services.pages.pages import PagesService
from services.pages.models import PageModel


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
