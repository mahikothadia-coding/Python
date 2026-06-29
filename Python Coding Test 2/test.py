def multiply(a, b):
    return a *b

def divide(a,b):
    return a/b

def subtract(a,b):
    return a-b

def add(a,b):
    return a+b
try:
    user_inputa = float(input("Enter a numbers of your choice:"))
    user_inputb = float(input("Enter another number of your choice:"))

    print("The result of multiplication is:", multiply(user_inputa, user_inputb))
    print("the result of these numbers dividing is : " , divide(user_inputa, user_inputb))
    print("The result of subtraction is:" , subtract(user_inputa,user_inputb))
    print("The result of addition is:" , add(user_inputa,user_inputb))
except ValueError:
    print ("value error. Please enter a number.")
except ZeroDivisionError:
    print("numbers divided by 0 is not possible. Please enter a number other than 0.") 
       