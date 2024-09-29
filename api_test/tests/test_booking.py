import faker
import pytest
import logging
from datetime import date, timedelta
from ..libs.bookingapi import (BookingAPI)

logger = logging.getLogger(__name__)


@pytest.fixture(scope="function")
def api():
    return BookingAPI("https://restful-booker.herokuapp.com")


class TestBooking:
    def test_get_booking_ids(self, api):
        response = api.get_booking_ids()
        assert response.status_code == 200
        # for i in response.json():
        #    logger.info(i)
        #    api.delete_booking(i["bookingid"])

    def test_create_booking(self, api):
        data = api.prepare_fake_booking()
        response = api.create_booking(data)
        assert response.status_code == 200
        booking_id = response.json()["bookingid"]

        response = api.get_booking(booking_id)
        assert response.status_code == 200
        booking_data = response.json()
        logging.info(f"Created booking: {booking_data}")
        assert booking_data['firstname'] == data["firstname"]
        assert booking_data['lastname'] == data["lastname"]

        api.delete_booking(booking_id)

    def test_update_booking(self, api):
        data = api.prepare_fake_booking()
        response = api.create_booking(data)
        assert response.status_code == 200
        booking_id = response.json()["bookingid"]
