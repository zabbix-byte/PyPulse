from .view import View

class SetView:
    def __init__(self, name: str, view: object, path_trigger:str) -> None:
        View(name, view, path_trigger)


class PathView:
    def __init__(self, name: str, path_trigger: str):
        self.name = name
        self.path_trigger = path_trigger

    def __call__(self, target_method):
        self.target_method = target_method
        return self.__get__

    def __get__(self, instance, owner):
        def wrapper(*args, **kwargs):
            # Access instance and owner (class) here         
            if instance:
                pass
            else:
                print("No instance accessed")
            return self.target_method(instance, *args, **kwargs)
        return wrapper