import pprint
import requests
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class BaseAPI:
    URL: str

    def __init__(self, url: str | None = None):
        self.url = url.strip("/") if url else self.URL
        self.session = requests.Session()

    def set_token(self, token):
        if token:
            self.session.cookies["token"] = token
        else:
            if "token" in self.session.cookies:
                del self.session.cookies["token"]

    def get(self, endpoint: str, query: dict | None = None,
            expected_status_code: int | list | None = None) -> requests.Response:
        """API GET Call.

        :param endpoint: API enpoint
        :param query: Optional query dictionary
        :param expected_status_code: Optional parameter to check the expected status code
        :return: Return API response as a requests.Response object
        """
        if query and isinstance(query, dict):
            logger.debug(f"GET {self.url=}, {endpoint=}, {query=}")
        else:
            logger.debug(f"GET {self.url}/{endpoint}")
        response = self.session.get(self.url + "/" + endpoint, params=query)
        ppjson = pprint.pformat(response.json(), indent=2,
                                compact=True) if response.status_code < 300 else response.content
        logger.debug(f"GET response: {response.status_code=}, JSON:\n{ppjson}")
        if expected_status_code:
            if isinstance(expected_status_code, int):
                expected_status_code = [expected_status_code]
            assert response.status_code in expected_status_code, f"Unexpected status code {response.status_code}. Expected status code(s): " + ", ".join(
                expected_status_code)
        return response

    def post(self, endpoint: str, data: dict,
             expected_status_code: int | list | None = None) -> requests.Response:
        """API POST Call.

        :param endpoint: API enpoint
        :param data: Data to post
        :param expected_status_code: Optional parameter to check the expected status code
        :return: Return API response as a requests.Response object
        """
        logger.debug(f"POST {self.url=}, {endpoint=}, {data=}")
        response = self.session.post(self.url + "/" + endpoint, json=data)
        logger.debug(f"POST response: {response.status_code=}")
        if expected_status_code:
            if isinstance(expected_status_code, int):
                expected_status_code = [expected_status_code]
            assert response.status_code in expected_status_code, f"Unexpected status code {response.status_code}. Expected status code(s): " + ", ".join(
                expected_status_code)
        return response

    def put(self, endpoint: str, data: dict,
            expected_status_code: int | list | None = None) -> requests.Response:
        """API PUT Call.

        :param endpoint: API enpoint
        :param data: Data to change
        :param expected_status_code: Optional parameter to check the expected status code
        :return: Return API response as a requests.Response object
        """
        response = self.session.put(self.url + "/" + endpoint, json=data)
        if expected_status_code:
            if isinstance(expected_status_code, int):
                expected_status_code = [expected_status_code]
            assert response.status_code in expected_status_code, f"Unexpected status code {response.status_code}. Expected status code(s): " + ", ".join(
                expected_status_code)
        return response

    def delete(self, endpoint: str,
               expected_status_code: int | list | None = None) -> requests.Response:
        """API DELETE Call.

        :param endpoint: API enpoint
        :param expected_status_code: Optional parameter to check the expected status code
        :return: Return API response as a requests.Response object
        """
        response = self.session.delete(self.url + "/" + endpoint)
        if expected_status_code:
            if isinstance(expected_status_code, int):
                expected_status_code = [expected_status_code]
            assert response.status_code in expected_status_code, f"Unexpected status code {response.status_code}. Expected status code(s): " + ", ".join(
                expected_status_code)
        return response
