from .ApiRestFullAuthTypes import Basic
from .vars import Controller


class ApiRestFull(Basic):
    def __init__(self) -> None:
        if Controller.BACKEND_AUTH.get('type') == 'basic':
            Basic.__init__(self,
                           Controller.BACKEND_AUTH.get('bearer'),
                           Controller.BACKEND_AUTH.get('bearer_header'),
                           Controller.BACKEND_AUTH.get('bearer_key'),
                           Controller.BACKEND_AUTH.get('url'),
                           Controller.LOGIN_URL,
                           Controller.REGISTER_URL,
                           Controller.LOGOUT_URL,
                           Controller.LOGIN_TOKEN_KEY
                           )
        else:
            raise ValueError(f'The auth type you not exists: {Controller.BACKEND_AUTH.get("type")}')
