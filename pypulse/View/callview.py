from .view import View


class CallView:
    def __init__(self, path: str) -> None:
        self.name = None
        self.view = None
        self.path_trigger = None

        for i in View.instances:
            if i.path_trigger == path:
                self.name = i.name
                self.view = i.view
                self.path_trigger = i.path_trigger
                break
    