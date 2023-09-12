from .aplication import Aplication
from .reader import ReadViews
from pypulse.View.view import View


class SetAplication:
    def __init__(self, name: str, primary: bool = False, primary_view_name: str = None) -> None:
        # finding the views of this aplication
        ReadViews.find_views_ho_are_using_the_decoratos(name)

        if primary_view_name is not None:
            self._check_if_primary_view_exists(primary_view_name, name)

        Aplication(name, primary, primary_view_name)

    def _check_if_primary_view_exists(self, primary_view_name: str, aplication_name: str):
        if f'{aplication_name}___{primary_view_name}' not in [i.name for i in View.instances]:
            raise ValueError(
                f'The Primary View Name <{primary_view_name}> dont exists in the views files, please check it')
