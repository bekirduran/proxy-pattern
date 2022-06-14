from abc import ABCMeta, abstractmethod


class IDbAccessProxy(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def getSystemInfo() -> str:
        pass
