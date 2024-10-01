import pytest
import os
import logging
from dotenv import load_dotenv
from booking_api_test.services.booking.booking_api import BookingAPI
from booking_api_test.services.auth.auth_api import AuthAPI

logger = logging.getLogger(__name__)
load_dotenv(".env")

BOOKING_URL = os.environ.get("BOOKING_API_URL", "https://restful-booker.herokuapp.com")
USERNAME = os.getenv("BOOKING_API_USERNAME")
PASSWORD = os.getenv("BOOKING_API_PASSWORD")


@pytest.fixture(scope="session")
def booking_api() -> "BookingAPI":
    return BookingAPI(BOOKING_URL)


@pytest.fixture(scope="session")
def auth() -> "AuthAPI":
    auth_object = AuthAPI(BOOKING_URL)
    auth_object.USERNAME = USERNAME
    auth_object.PASSWORD = PASSWORD
    return auth_object


@pytest.fixture(scope="session")
def token() -> str:
    logger.info("Authenticate")
    auth_object = AuthAPI(BOOKING_URL)
    return auth_object.create_token(username=USERNAME, password=PASSWORD)
