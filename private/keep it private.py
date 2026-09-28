class myClass:

    __privateVar = 27;

    def __privateMeth(self):
        print("I'm inside class myClass")

    def hello(self):
        print("Private Variable value:  ", myClass.__privateVar)    

object1 = myClass()
object1.hello()
object1.__privateMeth