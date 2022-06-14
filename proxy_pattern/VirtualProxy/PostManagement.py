from proxy_pattern.VirtualProxy.IRequestLayer import IRequestLayer


class PostManagement(IRequestLayer):
    "The actual real object PostManagement that the proxy is representing"

    def __init__(self):
        self.post_data = {
            "Virtual Proxy": "Virtual Proxy: An object that can cache parts of the real object, and then complete loading the full object when necessary.",
            "Remote Proxy": "Can relay messages to a real object that exists in a different address space.",
            "Protection Proxy": " Apply an authentication layer in front of the real object",
            "Smart Reference": "An object whose internal attributes can be overridden or replaced."
        }

    def requestPost(self):
        return self.post_data
