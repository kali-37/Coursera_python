employee_dict={
    1234:{"id":20,"name":"chanchal","department":"kitchen"},
    1235:{"id":23,"name":"hogrider","department":'Pig house'},
    1236:{"id":24,"name":"valkerine","department":"round house"
    }
}

def employee(id):
    return employee_dict[id]
a=int((input("Enter a number")))
print(employee(a))