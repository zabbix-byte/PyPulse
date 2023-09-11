from .aplication import Aplication
from .reader import ReadViews


class SetAplication:
    def __init__(self, name: str, primary: bool = False, primary_view_name: str = None) -> None:
        Aplication(name, primary, primary_view_name)

        # finding the views of this aplication
        ReadViews.find_views_ho_are_using_the_decoratos(name)
