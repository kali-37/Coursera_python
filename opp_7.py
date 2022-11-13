class school:
    a=5 # it is class variable and will be same for all child classes
    # Also, it lies between class and def __init__ .
    def __init__(shri,m,s):
        shri.m=m
        shri.s=s
    def output(shri):
        print(shri.m,shri.s)
        
    @classmethod # Representing below one is class method
    # i.e class school ko
    def output2(cls): # cls represents it's of class method
        print(cls.a) # and here real variable of class is only used.
# cls.a represent's it's of class variable so if no cls. then error as 
# a not reconized.
    @staticmethod # it is third method of method in class where 
    # we can add or append class.
    def output3():
        print("Hello this is static method")

c1=school(70,80)
c2=school(100,90)
c1.output() # if we want to run particular function
c2.output2()