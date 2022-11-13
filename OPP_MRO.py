class A:
    pass
class B:
    pass
class C(A):
    pass
print(C.mro()) # METHOD RESOLUTION ORDER. IT displays the order of class 
print(help(C())) # HELP FOR IT . q to quit help