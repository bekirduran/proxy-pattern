from proxy_pattern.ProtectionProxy.IDbAccessProxy import IDbAccessProxy
from proxy_pattern.ProtectionProxy.IStaff import IStaff


class Administrator(IStaff):
    _isAuth: bool = True
    dbaccess: IDbAccessProxy

    def isAuth(self) -> bool:
        return self._isAuth

    def tryAccess(self, dbaccess: IDbAccessProxy):
        self.dbaccess = dbaccess

    def getSystemInfo(self) -> str:
        try:
            return self.dbaccess.getSystemInfo()
        except:
            print("Error! try to access db with administrator")
        return ""
