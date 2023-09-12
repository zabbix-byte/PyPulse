from .aplication import Aplication


class GetAplication:
    @staticmethod
    def primary() -> Aplication:
        for i in Aplication.instances:
            if i.primary:
                return i
