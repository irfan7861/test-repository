
#Encapsulation is one of the fundamental concepts in object-oriented programming OOP.It describes the idea of wrapping
# data and the methods that work on data within one unit. This puts restrictions on accessing variables and methods
# directly and can prevent the accidental modification of data. To prevent accidental change, an object’s variable
# can only be changed by an object’s method. Those types of variables are known as private variable



class car:
    def __init__(self):
        self.__updatesoftware()
    def drive(self):
        print("driving")
    def __updatesoftware(self):
        print("updating software")

blackcar = car()
blackcar.drive()


class Base:
    def __init__(self):
        self._a = 2
class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("Calling protected member of base class: ")
        print(self._a)

obj = Derived()
obj2 = Base()
print(obj2.a)



































