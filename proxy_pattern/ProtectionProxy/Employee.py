from proxy_pattern.ProtectionProxy.IDbAccessProxy import IDbAccessProxy
from proxy_pattern.ProtectionProxy.IStaff import IStaff


class Employee(IStaff):
    dbaccess: IDbAccessProxy

    def isAuth(self) -> bool:
        return False

    def tryAccess(self, dbaccess: IDbAccessProxy):
        self.dbaccess = dbaccess

    def getSystemInfo(self) -> str:
        try:
            return self.dbaccess.getSystemInfo()
        except:
            print("Error! try to access db with employee ")
        return ""
