from .backend import BackendInstance


def login(username: str, password: str, **kwargs):
    return BackendInstance.instance.login(username, password, **kwargs)


def register(username: str, password: str, **kwargs):
    return BackendInstance.instance.register(username, password, **kwargs)


def logout():
    return BackendInstance.instance.logout()
