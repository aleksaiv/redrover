import logging

logger = logging.getLogger(__name__)


class TestBooking:
    def test_get_booking_ids(self, booking_api):
        logger.info("Get booking IDs")
        response = booking_api.get_booking_ids()
        logger.debug(f"IDs: {response.json()}")

    def test_create_booking(self, booking_api, token):
        logger.info(f"Created a new booking")
        data = booking_api.payloads.booking()
        response = booking_api.create_booking(data)
        logger.info(f"Created booking: {response.json()}")
        booking_id = response.json()["bookingid"]

        response = booking_api.get_booking(booking_id)
        booking_data = response.json()
        logging.info(f"Checking the created booking: {booking_data}")
        assert booking_data['firstname'] == data["firstname"]
        assert booking_data['lastname'] == data["lastname"]

        logger.info("Cleanup: Delete booking")
        booking_api.set_token(token)
        booking_api.delete_booking(booking_id)

    def test_update_booking(self, booking_api, token):
        booking_api.set_token(token)
        logger.info(f"Created a new booking")
        data = booking_api.payloads.booking()
        response = booking_api.create_booking(data)
        booking = response.json()
        logger.info(f"Booking info: {booking}")
        booking_id = booking["bookingid"]
        random_data = booking_api.payloads.booking()
        new_data = data.copy()
        new_data["firstname"] = random_data["firstname"]
        new_data["lastname"] = random_data["lastname"]
        logger.info(f"Change first name and last name to: {new_data['firstname']}, {new_data['lastname']}")
        response = booking_api.update_booking(booking_id, new_data)
        logger.info("Retrieve updated booking")
        response = booking_api.get_booking(booking_id)
        updated_booking = response.json()
        logger.info(f"Updated booking info: {updated_booking=}")
        assert updated_booking["firstname"] == new_data["firstname"]
        assert updated_booking["lastname"] == new_data["lastname"]
        logger.info("Cleanup: Delete booking")
        booking_api.delete_booking(booking_id)

    def test_delete_booking(self, booking_api, token):
        booking_api.set_token(token)
        logger.info(f"Created a new booking")
        data = booking_api.payloads.booking()
        response = booking_api.create_booking(data)
        logger.info(f"Booking info: {response.json()}")
        booking_id = response.json()["bookingid"]

        logger.info("Delete booking")
        booking_api.delete_booking(booking_id)

        logger.info("Check if it has been deleted")
        assert not booking_api.is_booking_exists(booking_id)
