from abc import ABCMeta, abstractmethod


class IRequestLayer(metaclass=ABCMeta):
    "An interface implemented by both the Proxy and Real Subject(PostManagement)"

    @staticmethod
    @abstractmethod
    def requestPost():
        "A method to implement"
