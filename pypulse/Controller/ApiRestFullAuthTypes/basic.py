import requests
import json

from .api_rest_methods import ApiRestMethods
from pypulse.Controller import Controller


class Basic(ApiRestMethods):
    def __init__(
        self,
        bearer: bool,
        bearer_header: str,
        bearer_key: str,
        url: str,
        login_url: str = None,
        register_url: str = None,
        logout_url: str = None,
        login_token_key: str = None,
    ):
        self.__url = url
        self.__login_url = login_url
        self.__logout_url = logout_url
        self.__bearer = bearer
        self.__bearer_header = bearer_header
        self.__bearer_key = bearer_key
        self.__access_token = None
        self.__api_session = requests.Session()
        self.__login_token_key = login_token_key
        self.__authenticated = False

    def __get_bearer(self):
        if self.__bearer:
            return {self.__bearer_header: f"{self.__bearer_key} {self.__access_token}", "Content-Type": "application/json"}
        return {}

    def login(self, username: str, password: str, headers: dict = {}):
        req = self.__api_session.post(
            f"{self.__url}{self.__login_url}",
            data={"username": username, "password": password},
            headers=headers,
        )

        if req.status_code > 299:
            self.__authenticated = False
            return self.__authenticated

        if self.__login_token_key:
            self.__access_token = json.loads(req.content).get(self.__login_token_key)
        else:
            self.__access_token = req.content

        self.__authenticated = True
        return self.__authenticated

    @FutureWarning
    def register(self):
        return

    def __filters(self, filters: dict) -> str:
        filters_string = ""
        for i in filters:
            filters_string += f'{i}{filters["spacer"]}{filters["type"]}{filters["assign"]}{filters["value"]}&'

        return filters_string[0:-1]

    def logout(self):
        self.__api_session.get(
            f"{self.__url}{self.__logout_url}", headers=self.__get_bearer()
        )
        self.__authenticated = False

    def get_data(self, endpoint: str, filters: dict = None) -> dict:
        if filters is None:
            req = self.__api_session.get(
                f"{self.__url}{endpoint}", headers=self.__get_bearer()
            )

        else:
            req = self.__api_session.get(
                f"{self.__url}{endpoint}?{self.__filters(filters)}", headers=self.__get_bearer()
            )
        if req.status_code > 299:
            return req.status_code

        return json.loads(req.content)

    def post_data(self, endpoint: str, filters: dict = None, body: dict = {}) -> dict:
        if filters is None:
            req = self.__api_session.post(
                f"{self.__url}{endpoint}", headers=self.__get_bearer(), data=json.dumps(body)
            )
        else:
            req = self.__api_session.post(
                f"{self.__url}{endpoint}?{self.__filters(filters)}",
                headers=self.__get_bearer(),
                data=body,
            )
        if req.status_code > 299:
            return req.status_code

        return json.loads(req.content)

    def set_manual_bearer(self, token: str) -> None:
        self.__access_token = token

    def authenticated(self) -> bool:
        if self.__authenticated:
            return self.__authenticated

        if Controller.CHECK_AUTH_URL:
            req = self.__api_session.get(
                f"{self.__url}{Controller.CHECK_AUTH_URL}", headers=self.__get_bearer()
            )

            if req.status_code == Controller.AUTH_FAIL_STATUS_CODE:
                return False

        if self.__access_token:
            self.__authenticated = True
            return True
        return False
