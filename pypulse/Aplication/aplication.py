class Aplication:
    instances = []
    
    def __init__(self, name: str, primary: bool = False, primary_view_name: str = None) -> None:
        self.name = name
        self.primary = primary
        self.primary_view_name = primary_view_name

        Aplication.instances.append(self)
