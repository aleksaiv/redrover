import logging
from booking_api_test.services.booking.models import BookingResponse, BookingModel
logger = logging.getLogger(__name__)


class TestBooking:
    def test_get_booking_ids(self, booking_api):
        logger.info("Get booking IDs")
        response = booking_api.get_booking_ids()
        logger.info(f"Number of booking IDs: {len(response.json())}")
        logger.debug(f"IDs: {response.json()}")

    def test_create_booking(self, booking_api, token):
        logger.info(f"Created a new booking")
        booking_payload = booking_api.payloads.booking()
        logger.info(f"{booking_payload=}")
        booking = booking_api.create_booking(booking_payload)
        logger.info(f"Created booking: {booking}")
        new_booking = booking_api.get_booking(booking.bookingid)
        logging.info(f"Checking created booking: {new_booking=}")
        assert new_booking.firstname == booking_payload.firstname
        assert new_booking.lastname == booking_payload.lastname

        logger.info("Cleanup: Delete booking")
        booking_api.set_token(token)
        booking_api.delete_booking(booking.bookingid)

    def test_update_booking(self, booking_api, token):
        booking_api.set_token(token)
        logger.info(f"Created a new booking")
        booking_payload = booking_api.payloads.booking()
        booking = booking_api.create_booking(booking_payload)
        logger.info(f"Booking info: {booking}")
        new_data = booking_payload.model_copy()
        random_data = booking_api.payloads.booking()
        new_data.firstname = random_data.firstname
        new_data.lastname = random_data.lastname
        logger.info(f"Change first name and last name to: {new_data.firstname}, {new_data.lastname}")
        response = booking_api.update_booking(booking.bookingid, new_data)
        logger.info("Retrieve updated booking")
        updated_booking = booking_api.get_booking(booking.bookingid)
        logger.info(f"Updated booking info: {updated_booking=}")
        assert updated_booking.firstname == new_data.firstname
        assert updated_booking.lastname == new_data.lastname
        logger.info("Cleanup: Delete booking")
        booking_api.delete_booking(booking.bookingid)

    def test_delete_booking(self, booking_api, token):
        booking_api.set_token(token)
        logger.info(f"Created a new booking")
        booking_payload = booking_api.payloads.booking()
        booking = booking_api.create_booking(booking_payload)
        logger.info(f"Booking info: {booking}")
        logger.info("Delete booking")
        booking_api.delete_booking(booking.bookingid)
        logger.info("Check if it has been deleted")
        assert not booking_api.is_booking_exists(booking.bookingid)
