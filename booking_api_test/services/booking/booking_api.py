import requests
from booking_api_test.libs.base_api import BaseAPI
from .payloads import Payloads


class BookingAPI(BaseAPI):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.payloads = Payloads()

    def get_booking_ids(self, expected_status_code: list | int | None = 200) -> requests.Response:
        return self.get("booking", expected_status_code=expected_status_code)

    def get_booking_ids_search(self, search: dict | None = None, expected_status_code: list | int | None = 200):
        return self.get("booking", query=search, expected_status_code=expected_status_code)

    def create_booking(self, data: dict, expected_status_code: list | int | None = 200) -> requests.Response:
        return self.post("booking", data=data, expected_status_code=expected_status_code)

    def get_booking(self, id: int, expected_status_code: list | int | None = 200) -> requests.Response:
        return self.get(f"booking/{id}", expected_status_code=expected_status_code)

    def is_booking_exists(self, id: int) -> bool:
        return self.get(f"booking/{id}").status_code == 200

    def update_booking(self, id: int, data: dict, expected_status_code: list | int | None = 200) -> requests.Response:
        return self.patch(f"booking/{id}", data=data, expected_status_code=expected_status_code)

    def delete_booking(self, id: int, expected_status_code: list | int | None = 201) -> requests.Response:
        return self.delete(f"booking/{id}", expected_status_code=expected_status_code)
