class Aplication:
    instances = []
    
    def __init__(self, name: str) -> None:
        self.name = name

        Aplication.instances.append(self)
