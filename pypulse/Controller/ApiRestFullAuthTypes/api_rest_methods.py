from abc import ABCMeta, abstractmethod


class ApiRestMethods(metaclass=ABCMeta):

    @abstractmethod
    def login(self):
        return

    @abstractmethod
    def register(self):
        return

    @abstractmethod
    def logout(self):
        return
