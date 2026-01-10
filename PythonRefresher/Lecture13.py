"""
functions
"""
def myFunc():
    print("Inside my function")

myFunc()

Name = "hassan"
def printMyName(name):
    print(f"hello {name}")

printMyName(Name)

def printColorRed():
    color = "red"
    print(color)
def multiply(a , b):
    return a*b
print(multiply(10,10))

def printList(list):
    for x in list:
        print(x)

list = [1,2,3,4,5]
printList(list)