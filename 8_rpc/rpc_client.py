import xmlrpclib
proxy = xmlrpclib.ServerProxy("http://localhost:8000/")
k = input("enter number:")
if proxy.is_even(k):
    ans = "even"
else:
    ans = "odd"
print str(k) + " is " + ans
