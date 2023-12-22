from .backend import BackendInstance


def login(username: str, password: str, **kwargs):
    return BackendInstance.instance.login(username, password, **kwargs)


def register(username: str, password: str, **kwargs):
    return BackendInstance.instance.register(username, password, **kwargs)


def logout():
    return BackendInstance.instance.logout()


def set_manual_bearer(token: str):
    return BackendInstance.instance.set_manual_bearer(token)


def authenticated():
    return BackendInstance.instance.authenticated()
