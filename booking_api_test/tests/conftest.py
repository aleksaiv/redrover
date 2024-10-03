import pytest
import logging
from booking_api_test.services.booking.booking_api import BookingAPI
from booking_api_test.services.auth.auth_api import AuthAPI
from booking_api_test.config import BOOKING_URL, USERNAME, PASSWORD

logger = logging.getLogger(__name__)


@pytest.fixture(scope="session")
def booking_api() -> "BookingAPI":
    return BookingAPI(BOOKING_URL)


@pytest.fixture(scope="session")
def token() -> str:
    logger.info("Authenticate")
    auth_object = AuthAPI(BOOKING_URL)
    return auth_object.create_token(username=USERNAME, password=PASSWORD)


@pytest.fixture(scope="function")
def auth(booking_api, token):
    booking_api.set_token(token)
    yield
    booking_api.set_token(None)
