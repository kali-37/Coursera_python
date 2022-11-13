class parent:
    def __init__(self):
        self.a=12
        
class child(parent):
    pass

child_instances=child() # instances of child classes 
print(child_instances.a) # calling a from instances > child > parent.
