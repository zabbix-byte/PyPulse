from .view import View


class SetView:
    def __init__(self, name: str, view: object, requirement_view: list, path_trigger: str) -> None:
        self._validate_new_view_consistance(name, path_trigger)
        View(name, view, requirement_view, path_trigger)

    def _validate_new_view_consistance(self, name, path_trigger):
        if len(View.instances) == 0:
            return

        if name in [i.name for i in View.instances]:
            raise KeyError(f'The view with the name {name} already exists')

        if path_trigger in [i.path_trigger for i in View.instances]:
            raise KeyError(
                f'The view with the path_trigger {path_trigger} already exists')

        for i in View.instances:
            current_path_instance_new = []
            current_paths_in_views_new = []

            current_path_instance = path_trigger.split('/')
            current_paths_in_views = i.path_trigger.split('/')

            # removing the variables and see if match

            for j in current_path_instance:
                if len(j) == 0:
                    current_path_instance_new.append(j)
                    continue
                if j[0] != '<' and j[-1] != '>':
                    current_path_instance_new.append(j)

            for j in current_paths_in_views:
                if len(j) == 0:
                    current_paths_in_views_new.append(j)
                    continue
                if j[0] != '<' and j[-1] != '>':
                    current_paths_in_views_new.append(j)

            if current_path_instance_new == current_paths_in_views_new:
                raise KeyError(
                    f'The view with the path_trigger {path_trigger} already exists, coincidende path: {i.path_trigger}')


def view(name: str, path_trigger: str):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)  # Call the original function
            return result
        return wrapper
    return decorator
