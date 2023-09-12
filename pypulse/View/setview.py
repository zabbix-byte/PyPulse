from .view import View


class SetView:
    def __init__(self, name: str, view: object, path_trigger: str) -> None:
        self._validate_new_view_consistance(name, path_trigger)
        View(name, view, path_trigger)

    def _validate_new_view_consistance(self, name, path_trigger):
        if len(View.instances) == 0:
            return

        if name in [i.name for i in View.instances]:
            raise KeyError(f'The view with the name {name} already exists')

        if path_trigger in [i.path_trigger for i in View.instances]:
            raise KeyError(
                f'The view with the path_trigger {path_trigger} already exists')


def view(name: str, path_trigger: str):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)  # Call the original function
            return result
        return wrapper
    return decorator
