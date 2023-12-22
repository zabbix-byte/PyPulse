from .vars import Controller
from .api_rest_full import ApiRestFull


class Backend(ApiRestFull):
    def __init__(self) -> None:
        if Controller.BACKEND_TYPE == 'api-restful':
            ApiRestFull.__init__(self)


class BackendInstance:
    instance = None

    def __init__(self) -> None:
        if not BackendInstance.instance:
            BackendInstance.instance = Backend()
