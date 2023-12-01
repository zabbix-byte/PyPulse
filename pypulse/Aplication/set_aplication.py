from .aplication import Aplication


class SetAplication:
    def __init__(self, name: str) -> None:
        self._check_if_aplication_is_already_registered(name)
        Aplication(name)

    def _check_if_aplication_is_already_registered(self, name:str):
        for i in Aplication.instances:
            if i.name == name:
                raise ValueError('The Aplication is already registered: {name}')
