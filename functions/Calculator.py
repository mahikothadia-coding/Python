def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    return a / b

print("Please select the Operation:" \
"a. Add " \
"b. subtract " \
"c. multiply " \
"d. divide")

choice = input("Please enter a choice (a/b/c/d): ")

num_1 = int(input("Please enter your first number:  "))
num_2 = int(input("Please enter your second number:  "))

if choice == 'a' :
    print(num_1, "+", num_2, "=", add(num_1,num_2))
elif choice == 'b':
    print(num_1, "-", num_2, "=", subtract(num_1,num_2))
elif choice == 'c':
    print(num_1, "*", num_2, "=", multiply(num_1,num_2))
elif choice == 'd':
    print(num_1, "/", num_2, "=", divide(num_1,num_2))
else :
    print("This is an invalid input!")

             