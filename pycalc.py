import sys

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    return a / b


a = None
b = None
op = None


    
a = int(input("Enter the first argument: "))
op = input("Enter the operation(*,/,+,-): ")
b = int(input("Enter the second argument: "))



if (op != None):
        if (op == "+"):
            print ("Sum: ", add(a, b))
        elif (op == "-"):
            print ("Difference: ", sub(a, b))
        elif (op == "*"):
            print ("Product: ", mult(a, b))
        elif (op == "/"):
            print ("Quotient: ", div(a, b))
else:
            print ("Invalid operation...")


