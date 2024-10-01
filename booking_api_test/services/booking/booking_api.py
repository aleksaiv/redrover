import requests
from booking_api_test.libs.base_api import BaseAPI
from .payloads import Payloads


class BookingAPI(BaseAPI):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.payloads = Payloads()

    def get_booking_ids(self, search: dict | None = None) -> requests.Response:
        """
        Return the ids of all the bookings that exist within the API.
        Can take optional query strings to search and return a subset of booking ids.

        :param search: dict with query strings (accept params: firstname, lastname, checkin, checkout)
        :return: Return API call result as a requests.Response object
        """
        if search and isinstance(search, dict):
            return self.get("booking", query=search, expected_status_code=200)
        return self.get("booking", expected_status_code=200)

    def create_booking(self, data: dict) -> requests.Response:
        """
        Create a new booking.

        :param data: booking params (firstname, lastname, etc.)
        :return: API call result as a requests.Response object
        """
        return self.post("booking", data=data, expected_status_code=200)

    def get_booking(self, id: int) -> requests.Response:
        """
        Get a booking information

        :param id: Booking id
        :return: API call result as a requests.Response object
        """
        return self.get(f"booking/{id}", expected_status_code=200)

    def is_booking_exists(self, id: int) -> requests.Response:
        """
        Check if booking exists

        :param id: Booking id
        :return: Return True if booking exists
        """

        return self.get(f"booking/{id}").status_code == 200

    def update_booking(self, id: int, data: dict) -> requests.Response:
        return self.put(f"booking/{id}", data, expected_status_code=200)

    def delete_booking(self, id: int) -> requests.Response:
        return self.delete(f"booking/{id}", expected_status_code=201)
