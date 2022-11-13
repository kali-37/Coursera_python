try:
    file=open("Test.txt",mode="r")
    data=file.readline()
    print(data)
    file.close()
except  FileNotFoundError as e:
    print("Error File wast not found error type",e)
with open('Test.txt', 'rw') as file:

    print(type(file))