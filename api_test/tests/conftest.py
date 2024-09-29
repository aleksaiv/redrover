import pytest
import os
from dotenv import load_dotenv
from api_test.services.booking.booking_api import BookingAPI
from api_test.services.auth.auth_api import AuthAPI

load_dotenv("../.env")

URL = os.environ.get("BOOKING_API_URL")
USERNAME = os.getenv("BOOKING_API_USERNAME")
PASSWORD = os.getenv("BOOKING_API_PASSWORD")


@pytest.fixture(scope="session")
def api() -> "BookingAPI":
    return BookingAPI(URL)


@pytest.fixture(scope="session")
def auth() -> "AuthAPI":
    auth_object = AuthAPI(URL)
    auth_object.USERNAME = USERNAME
    auth_object.PASSWORD = PASSWORD

    return auth_object
