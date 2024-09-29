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
        #for i in response.json():
        #    logger.info(i)
        #    api.delete_booking(i["bookingid"])
    def test_create_booking(self, api):
        f = faker.Faker()
        d1 = f.date_between_dates(date_start=date.today(), date_end=date.today() + timedelta(days=365))
        d2 = f.date_between_dates(date_start=d1, date_end=date.today() + timedelta(days=365))
        first_name = f.first_name()
        last_name = f.last_name()
        data = {"firstname": first_name,
                "lastname": last_name,
                "totalprice": f.pyfloat(3,2, True, min_value=0.01, max_value=999.99),
                "depositpaid": f.boolean(70),
                "bookingdates": {"checkin": str(d1), "checkout": str(d2)},
                "additionalneeds": "cofee"}
        response = api.create_booking(data)
        assert response.status_code == 200
        booking_id = response.json()["bookingid"]
        response = api.get_booking(booking_id)
        assert response.status_code == 200
        booking_data = response.json()
        logging.info(f"Created booking: {booking_data}")
        assert booking_data['firstname'] == first_name
        assert booking_data['lastname'] == last_name
