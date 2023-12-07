import requests
import json

from .api_rest_methods import ApiRestMethods


class Basic(ApiRestMethods):
    def __init__(self, bearer: bool,
                 bearer_header: str,
                 bearer_key: str,
                 url: str,
                 login_url: str = None,
                 register_url: str = None,
                 logout_url: str = None,
                 login_token_key: str = None
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

    def __get_bearer(self):
        return {self.__bearer_header: f'{self.__bearer_key} {self.__access_token}'}

    def login(self, username: str, password: str, headers: dict = {}):
        req = self.__api_session.post(
            f'{self.__url}{self.__login_url}',
            data={
                'username': username,
                'password': password
            },
            headers=headers
        )

        if req.status_code > 299:
            return False

        if self.__login_token_key:
            self.__access_token = json.loads(req.content).get(self.__login_token_key)
        else:
            self.__access_token = req.content

        return True

    @FutureWarning
    def register(self):
        return

    def logout(self):
        if self.__bearer:
            headers = self.__get_bearer()

        self.__api_session.get(
            f'{self.__url}{self.__logout_url}',
            headers=headers
        )
