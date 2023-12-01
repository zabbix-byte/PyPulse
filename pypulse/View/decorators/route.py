import random
import string

from pypulse.Aplication.vars import Vars


def view(name: str, path_trigger: str):
    def inner(function):
        def wrapper(*args, **kwargs):
            return function(*args, **kwargs)

        token = ''.join(random.choices(
            string.ascii_lowercase + string.digits, k=8))
        Vars.VIEWS.append(token)

        wrapper.__name__ = token
        wrapper.route = path_trigger
        wrapper.name = name

        wrapper.redirect = False

        return wrapper
    return inner
