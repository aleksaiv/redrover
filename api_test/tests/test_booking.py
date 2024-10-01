import pytest
import logging
from api_test.services.booking.booking_api import BookingAPI
from api_test.services.auth.auth_api import AuthAPI
logger = logging.getLogger(__name__)

import os

class TestBooking:
    def test_get_booking_ids(self, api):
        logger.info("Test get booking IDs")
        response = api.get_booking_ids()
        assert response.status_code == 200
        logger.debug(f"IDs: {response.json()}")

    def test_create_booking(self, api, auth):
        logger.info("Test create booking")
        data = api.payloads.booking()
        response = api.create_booking(data)
        assert response.status_code == 200
        logger.info(f"Create new booking: {response.json()}")
        booking_id = response.json()["bookingid"]

        response = api.get_booking(booking_id)
        assert response.status_code == 200
        booking_data = response.json()
        logging.info(f"Created booking: {booking_data}")
        assert booking_data['firstname'] == data["firstname"]
        assert booking_data['lastname'] == data["lastname"]

        logger.info("Authenticate")
        token = auth.create_token(auth.USERNAME, auth.PASSWORD)
        api.set_token(token)
        api.delete_booking(booking_id)

    def test_update_booking(self, api, auth):
        logger.info("Test update booking")
        data = api.payloads.booking()
        response = api.create_booking(data)
        assert response.status_code == 200
        booking = response.json()
        logger.info(f"Booking info: {booking}")
        booking_id = booking["bookingid"]

        logger.info("Authenticate")
        token = auth.create_token("admin", "password123")
        api.set_token(token)

        random_data = api.payloads.booking()
        new_data = data.copy()
        new_data["firstname"] = random_data["firstname"]
        new_data["lastname"] = random_data["lastname"]
        logger.info(f"{new_data=}")
        logger.info(f"Change first name and last name to: {new_data['firstname']}, {new_data['lastname']}")
        response = api.update_booking(booking_id, new_data)
        assert response.status_code == 200

        logger.info("Fetch updated booking")
        response = api.get_booking(booking_id)
        assert response.status_code == 200
        updated_booking = response.json()
        logger.info(f"Updated booking: {updated_booking=}")
        assert updated_booking["firstname"] == new_data["firstname"]
        assert updated_booking["lastname"] == new_data["lastname"]

        api.delete_booking(booking_id)

    def test_delete_booking(self, api, auth):
        logger.info("Test delete booking")
        data = api.payloads.booking()
        response = api.create_booking(data)
        assert response.status_code == 200
        logger.info(f"Create new booking: {response.json()}")
        booking_id = response.json()["bookingid"]

        logger.info("Authenticate")
        token = auth.create_token("admin", "password123")
        api.set_token(token)
        logger.info("Delete booking")
        api.delete_booking(booking_id)

        logger.info("Check if it has been deleted")
        response = api.get_booking(booking_id)
        assert response.status_code == 404

