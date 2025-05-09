import os
from dataclasses import asdict

import requests
from requests import Response
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
from pydantic import BaseModel

from helpers.allure import Allure
from helpers.checkers import Checkers
from helpers.service_data import ServiceDataModel

load_dotenv()


class ApiClient:
    def __init__(self) -> None:
        self.base_url = os.getenv("BASE_URL")
        self.credentials = os.getenv("USERNAME"), os.getenv("PASSWORD")
        self.response = None

    def request(
        self,
        method: str,
        endpoint: str,
        expected_code: int,
        validate: bool,
        model: BaseModel,
        **kwargs: dict
    ) -> Response:
        self.url = self.base_url + endpoint
        self.response = requests.request(
            method=method,
            url=self.url,
            auth=HTTPBasicAuth(*self.credentials),
            json=asdict(self.payloads),
            **kwargs
        )
        Allure.attach_response_body(self.response)
        Checkers.check_status_code(expected_code, self.response.status_code)
        if validate:
            self.model = Checkers.validate(model, self.response.json())
            if self.payloads:
                return ServiceDataModel(self.payloads, self.model)
            return ServiceDataModel(self.model)

    def get(self, **kwargs: dict) -> Response:
        return self.request("GET", **kwargs)

    def post(self, **kwargs: dict) -> Response:
        return self.request("POST", **kwargs)

    def delete(self, **kwargs: dict) -> Response:
        return self.request("DELETE", **kwargs)
