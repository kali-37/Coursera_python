menu=["espresso","mocha","latte","cappuccino","cortado","americano"]

def find_coffee(coffee):
    if coffee[0]=='c':
        return coffee
    
map_coffee=map(find_coffee,menu)
print(map_coffee)
# This  prints <map object at ...>  

# Now, below gonna display real thingi i.e starts with 'c' indeed.

for x in map_coffee:
    print(x)

filter_coffee=filter(find_coffee,menu)
print(filter_coffee)

# It dosen't print NONE in ans
for x in filter_coffee:
    print(x)