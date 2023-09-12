from .view import View


class SetView:
    def __init__(self, name: str, view: object, path_trigger: str) -> None:
        View(name, view, path_trigger)


def view(name: str, path_trigger: str):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)  # Call the original function
            return result
        return wrapper
    return decorator
