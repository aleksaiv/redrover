import requests

from ...libs.base_api import BaseAPI
from .payloads import Payloads


class MyAPI(BaseAPI):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.payloads = Payloads()

    def get_testcases(self, expected_status_code: list | int | None = 200) -> requests.Response:
        return self.get("testcases", expected_status_code=expected_status_code)

    def create_testcase(self, data: dict, expected_status_code: list | int | None = 200) -> requests.Response:
        return self.post("testcases", data=data, expected_status_code=expected_status_code)

    def get_testcase(self, id: int, expected_status_code: list | int | None = 200) -> requests.Response:
        return self.get(f"testcases/{id}", expected_status_code=expected_status_code)

    def is_testcase_exists(self, id: int) -> bool:
        return self.get(f"testcases/{id}").status_code == 200

    def update_testcase(self, id: int, data: dict, expected_status_code: list | int | None = 200) -> requests.Response:
        return self.patch(f"testcases/{id}", data=data, expected_status_code=expected_status_code)

    def delete_testcase(self, id: int, expected_status_code: list | int | None = 200) -> requests.Response:
        return self.delete(f"testcases/{id}", expected_status_code=expected_status_code)
