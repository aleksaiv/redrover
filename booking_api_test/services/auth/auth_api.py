import logging
from booking_api_test.libs.base_api import BaseAPI

logger = logging.getLogger(__name__)


class AuthAPI(BaseAPI):
    USERNAME: str
    PASSWORD: str

    def create_token(self, username: str, password: str) -> str:
        """
        Authenticate and return token.

        :param username: Username
        :param password: Password
        :return: Return token
        """
        logger.debug(f"Create token: {username=}, {password=}")
        response = self.post("auth", data={"username": username, "password": password}, expected_status_code=200)
        data = response.json()
        logger.debug(f"Auth result: {data}")
        assert "token" in data, "Access denied"
        return response.json()["token"]
