from .get import View


class Property:
    def __init__(self, func) -> None:
        self.func = classmethod(func)

    def __get__(self, *args):
        return self.func.__get__(*args)()


class Model:
    @Property
    def view(cls):
        if not cls:
            return
        return View(model=cls)

    class Meta:
        pass
