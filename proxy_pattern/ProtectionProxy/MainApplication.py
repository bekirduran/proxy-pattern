from proxy_pattern.ProtectionProxy.Administrator import Administrator
from proxy_pattern.ProtectionProxy.DbAccessProxy import DbAccessProxy
from proxy_pattern.ProtectionProxy.Employee import Employee

if __name__ == "__main__":

    admin = Administrator()
    system = DbAccessProxy(admin)
    admin.tryAccess(system)
    print(admin.getSystemInfo())

    print("------------------")

    user = Employee()
    system = DbAccessProxy(user)
    user.tryAccess(system)
    print(user.getSystemInfo())
