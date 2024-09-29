import faker
from datetime import date, timedelta
import requests
from .baseapi import BaseAPI


class BookingAPI(BaseAPI):
    def get_booking_ids(self, search: dict | None = None) -> requests.Response:
        """
        Return the ids of all the bookings that exist within the API.
        Can take optional query strings to search and return a subset of booking ids.

        :param search: dict with query strings (accept params: firstname, lastname, checkin, checkout)
        :return: Return API call result as a requests.Response object
        """
        if search and isinstance(search, dict):
            return self.get("booking", query=search)
        return self.get("booking")

    def create_booking(self, data: dict) -> requests.Response:
        """
        Create a new booking.

        :param data: booking params (firstname, lastname, etc.)
        :return: API call result as a requests.Response object
        """
        return self.post("booking", data=data)

    def get_booking(self, id: int) -> requests.Response:
        """
        Get a booking information

        :param id: Booking id
        :return: API call result as a requests.Response object
        """
        return self.get(f"booking/{id}")

    def update_booking(self, id: int, data: dict) -> requests.Response:
        return self.put(f"booking/{id}", data)

    def delete_booking(self, id) -> requests.Response:
        return self.delete(f"booking/{id}")

    def prepare_fake_booking(self) -> dict:
        f = faker.Faker()
        d1 = f.date_between_dates(date_start=date.today(), date_end=date.today() + timedelta(days=365))
        d2 = f.date_between_dates(date_start=d1, date_end=date.today() + timedelta(days=365))
        first_name = f.first_name()
        last_name = f.last_name()
        data = {"firstname": first_name,
                "lastname": last_name,
                "totalprice": f.pyfloat(3, 2, True, min_value=0.01, max_value=999.99),
                "depositpaid": f.boolean(70),
                "bookingdates": {"checkin": str(d1), "checkout": str(d2)},
                "additionalneeds": "cofee"}
        return data
