from proxy_pattern.ProtectionProxy.IDbAccessProxy import IDbAccessProxy
from proxy_pattern.ProtectionProxy.IStaff import IStaff


class DbAccessProxy(IDbAccessProxy):
    _staff: IStaff
    systemInfo: str

    def __init__(self, staff):
        self._staff = staff

    def getSystemInfo(self) -> str:
        if self._staff.isAuth():
            self.systemInfo = ""
            try:
                self.systemInfo = ":::This is secret system Info:::\n" \
                                  "OS: Windows 10\n" \
                                  "Net user: Morph\n" \
                                  "Location: Ankara,Turkey\n" \
                                  "GitHub: @bekirduran\n" \
                                  "Stackoverflow: @bekirduran"
                return self.systemInfo
            except:
                print("Error! Dbaccessproxy class")
            return ""
        else:
            return "Not Authorized to view system info."
