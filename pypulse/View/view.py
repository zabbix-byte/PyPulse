class View:
    instances = []

    def __init__(self, name: str, view: object, path_trigger: str) -> None:
        self.name = name
        self.view = view
        self.path_trigger = path_trigger

        View.instances.append(self)
