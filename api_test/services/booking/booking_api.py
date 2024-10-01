import requests
from api_test.libs.base_api import BaseAPI
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

    def delete_booking(self, id: int) -> requests.Response:
        return self.delete(f"booking/{id}")
