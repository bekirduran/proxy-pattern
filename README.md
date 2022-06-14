# Proxy Pattern Example
### The Proxy design pattern is a class functioning as an interface to another class or object. A Proxy could be for anything, such as a network connection, an object in memory, a file, or anything else you need to provide an abstraction between.
Types of proxies,

- <b>Virtual Proxy:</b> An object that can cache parts of the real object, and then complete loading the full object when necessary.

- <b>Remote Proxy:</b>  Can relay messages to a real object that exists in a different address space.

- <b>Protection Proxy:</b>  Apply an authentication layer in front of the real object.

- <b>Smart Reference:</b>  An object whose internal attributes can be overridden or replaced.

## In this example i try to explain the Virtual Proxy lets look at:

### IRequestLayer.py class is interface 
<img src=/screen_shots/ss1.JPG >

### PostManagement.py class is implemented from IRequestLayer.py
<img src=/screen_shots/ss2.JPG >

### PostProxy.py class is implemented from IRequestLayer.py
<img src=/screen_shots/ss3.JPG >

### MainApplication.py we called our classes and run our code
<img src=/screen_shots/ss4.JPG >

### Output: as you can see in the first call, it took the data from post management and brought it, then brought it from the cache.
<img src=/screen_shots/ss5.JPG >

### With help of <b>Virtual Proxy Design Pattern</b>:
- A virtual proxy can cache elements of a real subject before loading the full object into memory.. With the memory saving technique, The advantage of this approach is a faster application start-up time, as it is not required to created and load all of the application objects.


<br/>
<br/>
<br/>

## In this example i try to explain the Protection Proxy lets look at:
### In general, objects in an application interact with each other to implement the overall application functionality. Most application object are generally accessible to all other objects in the application. At times, it may be necessary to restrict the accessibility of an object only to a limited set of client objects based on their access rights. When a client object tries to access such an object, the client is given access to the services provided by the object only if the client can furnish proper authentication credentials. In such cases, a separate object can be designated with the responsibility of verifying the access privileges of different client objects when they access the actual object. In other words, every client must successfully authenticate with this designated object to get access to the actual object functionality. Such an object with which a client needs to authenticate to get access to the actual object can be referred as an object authenticator which is implemented using the Protection Proxy.




### IStaff.py class is interface
<img src=/screen_shots/ss6.JPG >

### IDbAccessProxy.py is interface
<img src=/screen_shots/ss7.JPG >

### Employee.py class is implemented from IStaff.py
<img src=/screen_shots/ss8.JPG >

### Administrator.py class is implemented from IStaff.py
<img src=/screen_shots/ss9.JPG >

### DbAccessProxy.py class some busines logic operation class
<img src=/screen_shots/ss10.JPG >

### Output: Thanks to the protection proxy, we made the authorization restriction thanks to the interfaces.
<img src=/screen_shots/ss11.JPG >

### With help of <b>Protection Proxy Design Pattern</b>:
- A protection proxy can provide an authentication layer. For example, an NGINX proxy can add Basic Authentication restriction to an HTTP request.



