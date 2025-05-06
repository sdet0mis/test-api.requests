import os

import requests
from requests import Response
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

from helpers.allure import Allure
from helpers.checkers import Checkers

load_dotenv()


class ApiClient:
    def __init__(self) -> None:
        self.base_url = os.getenv("BASE_URL")
        self.credentials = os.getenv("USERNAME"), os.getenv("PASSWORD")
        self.response = None

    def request(
        self, method: str, endpoint: str, expected_code: int, **kwargs: dict
    ) -> Response:
        self.url = self.base_url + endpoint
        self.response = requests.request(
            method=method,
            url=self.url,
            auth=HTTPBasicAuth(*self.credentials),
            **kwargs
        )
        Allure.attach_response_body(self.response)
        Checkers.check_status_code(expected_code, self.response.status_code)
        return self.response

    def post(self, **kwargs: dict) -> Response:
        return self.request("POST", **kwargs)

    def delete(self, **kwargs: dict) -> Response:
        return self.request("DELETE", **kwargs)
