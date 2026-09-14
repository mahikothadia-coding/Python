class Employee:
    def __init__(self):
        print("Employee created")

    def __del__(self):
        print("Destructer called")

def Create_obj():
    print("Making object.....")
    obj = Employee()
    print("function end ......")
    return object

print("Calling Create_obj()  function...")
obj = Create_obj()
print("Program end....")





