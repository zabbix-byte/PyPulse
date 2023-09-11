from .aplication import Aplication

class SetAplication():
    def __init__(self, name: str, path: str, primary: bool = False, primary_view_name: str = None) -> None:
        Aplication(name, path, primary, primary_view_name)
