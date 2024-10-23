import pytest
import logging
from ..services.testcases.myapi import MyAPI
from ..config import API_URL

logger = logging.getLogger(__name__)


@pytest.fixture(scope="session")
def api() -> "MyAPI":
    return MyAPI(API_URL)

