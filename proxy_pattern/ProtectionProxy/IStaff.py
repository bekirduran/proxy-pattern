from abc import ABCMeta, abstractmethod


class IStaff(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def isAuth() -> bool:
        pass

    @staticmethod
    @abstractmethod
    def tryAccess(dbaccess):
        pass
