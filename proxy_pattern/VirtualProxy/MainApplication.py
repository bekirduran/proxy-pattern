from proxy_pattern.VirtualProxy.PostProxy import PostProxy
import time

if __name__ == "__main__":
    proxy = PostProxy()
    print(proxy.requestPost().values())

    print("----------------------------")
    print("Someting someting happend")
    time.sleep(3)
    print("----------------------------")

    print(proxy.requestPost()["Virtual Proxy"])
