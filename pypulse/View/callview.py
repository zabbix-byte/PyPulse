from .view import View


class CallView:
    def __init__(self, view_name: str) -> None:
        self.name = None
        self.view = None
        self.path_trigger = None

        for i in View.instances:
            if i.name == view_name:
                self.name = i.name
                self.view = i.view
                self.path_trigger = i.path_trigger
                break
