class View:
    instances = []

    def __init__(self, name: str, view: object,requirement_view:list, path_trigger: str) -> None:
        self.name = name
        self.view = view
        self.requirement_view = requirement_view
        self.path_trigger = path_trigger

        View.instances.append(self)
