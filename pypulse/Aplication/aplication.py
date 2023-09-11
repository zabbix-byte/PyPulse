class Aplication:
    instances = []
    
    def __init__(self, name: str, path: str, primary: bool = False, primary_view_name: str = None) -> None:
        self.name = name
        self.path = path
        self.primary = primary
        self.primary_view_name = primary_view_name

        Aplication.instances.append(self)
