from .backend import BackendInstance


def login(username: str, password: str, **kwargs):
    BackendInstance.instance.login(username, password, **kwargs)


def register(username: str, password: str, **kwargs):
    BackendInstance.instance.register(username, password, **kwargs)


def logout():
    BackendInstance.instance.logout()
