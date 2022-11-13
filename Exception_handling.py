def divide_by(a,b):
    return a/b

# It gives a error that is ZeroDivisionError().

#    print(divide_by(40,0))

# But IF I do this it will throw my error as error .
#try statment will try the code first 
try:
    ans=divide_by(40, 0)
    #except: can be done to print something went worng but if i want to specify 
except:
    print("Something went wrong.!")
    
print("\033[33m Type:1 \033[35m Next type to specify error as  \033[0m")

try:
    ans=divide_by(40, 0)
    #What was the error actually then except Exception as e is done.
    
except  Exception as e:
    print("Something went wrong.!",e)
    
print("\033[33m Type:2 \033[35m Next type to specify error as  \033[0m")

try:
    ans=divide_by(40, 0)
    #What was the error actually then except Exception as e is done.
    
except  Exception as e:
    print("Something went wrong.!")
    print(e.__class__)
    
print("\033[33m Type:3 \033[35m Next type to specify error as  \033[0m")

try:
    ans=divide_by(40, 0)
except ZeroDivisionError as e:
    print(e," We cannot divide by zero .")
except Exception as e:
    print("Something went worng",e)

print("\033[33m Type:4  \033[35m Acutal type \033[32m Next type to specify error as  \033[0m")
print(divide_by(40, 0))