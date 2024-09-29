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

    def get(self, endpoint: str, query: dict | None = None) -> requests.Response:
        """API GET Call.

        :param endpoint: API enpoint
        :param query: Optional query dictionary
        :return: Return API response as a requests.Response object
        """
        if query and isinstance(query, dict):
            logger.debug(f"GET {self.url=}, {endpoint=}, {query=}")
        else:
            logger.debug(f"GET {self.url}/{endpoint}")
        response = self.session.get(self.url + "/" + endpoint, params=query)
        logger.debug(f"GET response: {response.status_code=}, JSON:\n{pprint.pformat(response.json(), indent=2,compact=True) if response.status_code < 300 else response.content}")
        return response

    def post(self, endpoint: str, data: dict) -> requests.Response:
        logger.debug(f"POST {self.url=}, {endpoint=}, {data=}")
        return self.session.post(self.url + "/" + endpoint, json=data)

    def put(self, endpoint: str, data: dict) -> requests.Response:
        return self.session.put(self.url + "/" + endpoint, json=data)

    def delete(self, endpoint: str) -> requests.Response:
        return self.session.delete(self.url + "/" + endpoint)
