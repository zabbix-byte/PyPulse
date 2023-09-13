from .aplication import Aplication
from .reader import ReadViews
from pypulse.View.view import View


class SetAplication:
    def __init__(self, name: str) -> None:
        # finding the views of this aplication
        self._check_if_aplication_is_already_registered(name)
        ReadViews.find_views_ho_are_using_the_decoratos(name)
        Aplication(name)

    def _check_if_aplication_is_already_registered(self, name:str):
        for i in Aplication.instances:
            if i.name == name:
                raise ValueError('The Aplication is already registered: {name}')
        