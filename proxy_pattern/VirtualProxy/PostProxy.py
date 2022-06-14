from proxy_pattern.VirtualProxy.IRequestLayer import IRequestLayer
from proxy_pattern.VirtualProxy.PostManagement import PostManagement


class PostProxy(IRequestLayer):
    """
   The proxy. In this case the proxy will act as a cache for
   `enormous_data` and only populate the enormous_data when it
   is actually necessary
   """

    def __init__(self):
        self.post_data = {}
        self.post_management = PostManagement()

    def requestPost(self):
        """
        Using the proxy as a cache, and loading data into it only if
        it is needed
        """
        if self.post_data == {}:
            print("::::Pulling data from Post Management::::\n")
            self.post_data = self.post_management.requestPost()
            return self.post_data
        print("::::Pulling data from Proxy Cache::::\n")
        return self.post_data
