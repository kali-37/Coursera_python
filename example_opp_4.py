class Playlips:
    
    
    a=5 # it 'a' is class variable which remains in between init and class decleration 
    # at it's gonna be remain same for all object going made later
    
    
    
    # init is called by itself always when object of the class is made like:
    # object of class means { c=Playlips(3,"sy",4) } here, c is object 
    
    def __init__(self,payment,name,amount) -> None: # here self can be replaced 
        # by any name but all must be replaced
        self.payment=payment
        self.name=name
        self.amount=amount 
        
    def pay(self):
        self.payment="yes"
    
    def status(self):
        if self.payment=="yes":
            return self.name +" is paid " +str(self.amount)
        else:
            return self.name +" is not paid yet"
nanthan=Playlips("no","nanthan",1100)        
roger=Playlips("no","roger",1242)
print(nanthan.status(), "\n"+roger.status())

print("\x1b[32m \n After Payment of nanthan only.")
nanthan.pay()
print("\033[35m",nanthan.status(),"\n",roger.status(),"\033[0m")