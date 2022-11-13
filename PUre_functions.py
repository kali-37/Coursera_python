my_list=[1,2,3]

def add_to_list(lst,item):
    # If we don't copy then whole of my_list is changing from functions and it's not gonna
    # be  pure function so , copying it to other and adding the item 4.
    nl=lst.copy()
    nl.append(item)
    return nl

new_list= add_to_list(my_list,4)

# This will print with appended item
print(new_list)
# It will not make any sense at all and remains pure as previous.
print(my_list)