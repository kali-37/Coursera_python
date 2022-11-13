print("Hello World")
print("How are you.")

# to print in from new line we can do this in python and bash too.
# any amount of space is okay in python as we can see in 1+7 has more space and having (\) we can 
# add +8 totaling a=1+7+8
a=1 +        7\
+8
print(a)


a="make"
b="goods"

# this is used to concanete strings the numbers 0f '{}' specifies the number of format to be printed.
# If below has only "{}" then only make would have printed.
print("Hello,{}{} ".format(a,b))

#this is also concanete the strings.
print("Hello "+str(a)+str(b))