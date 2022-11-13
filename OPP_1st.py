class Myclass:
    a=5
    print("Hello")
    
    # if we don't write self in below line than 
    # Traceback (most recent call last):
#   File "location/.//.///.// >>", line 12, in <module>
    # print(myc.hello())
# TypeError: hello() takes 0 positional arguments but 1 was given
    def hello(anyname_no_need_to_enter_self_only):
        print("HI , Dood !")
    
myc=Myclass()
print(Myclass.a)
print(myc.a)
print(myc.hello())