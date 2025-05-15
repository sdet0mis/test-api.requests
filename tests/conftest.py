from typing import Generator

import pytest

from helpers.db import DBConnector


@pytest.fixture(scope="session", autouse=True)
def db() -> Generator[DBConnector]:
    db = DBConnector()
    yield db
    db.disconnect()
