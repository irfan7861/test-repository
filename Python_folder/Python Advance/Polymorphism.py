
# Python can use different types of classes, in the same way, using Polymorphism. To serve this purpose, one can create a
# loop that iterates through a tuple of objects. Post which, one can call the methods without having a look at the type of
# class to which the object belongs to



class Rabbit():
    def age(self):
        print("This function determines the age of Rabbit.")

    def color(self):
        print("This function determines the color of Rabbit.")

class Horse():
    def age(self):
        print("This function determines the age of Horse.")

    def color(self):
        print("This function determines the color of Horse.")

obj1 = Rabbit()
obj2 = Horse()
for type in (obj1, obj2): # creating a loop to iterate through the obj1, obj2
    type.age()
    type.color()



# class Tv():
#     def price(self):
#         print("Price of tv")
#     def colour(self):
#         print("Colour of tv")
#     def inches(self):
#         print("Tv size is 32 inch")
#
# class Mobile():
#     def price(self):
#         print("price of mobile")
#     def colour(self):
#         print("Colour of mobile")
#     def inches(self):
#         print("mobile size is 5 inch")
#
# T1 = Tv()
# M1 = Mobile()
#
#
# for type in (T1, M1):# creating a loop to iterate through the T1, M1
#     type.price()
#     type.colour()
#     type.inches()


# class Animal:
#     def type(self):
#         print("Various types of animals")
#
#     def age(self):
#         print("Age of the animal.")
#
# class Rabbit(Animal):
#     def age(self):
#         print("Age of rabbit.")
#
#
# class Horse(Animal):
#     def age(self):
#         print("Age of horse.")
#
#
# obj_animal = Animal()
# obj_rabbit = Rabbit()
# obj_horse = Horse()
#
# obj_animal.type()
# obj_animal.age()
#
# obj_rabbit.type()
# obj_rabbit.age()
#
# obj_horse.type()
# obj_horse.age()


#polymorphism using with inheritance

# class Fruits:
#     def type(self):
#         print("Various type of fruits")
#     def colour(self):
#         print("colour of fruits")

# class Apple(Fruits):
#     def colour(self):
#         print("colour of apple")

# class Banana(Fruits):
#     def colour(self):
#         print("colour of banana")

# obj_fruit = Fruits()
# obj_apple = Apple()
# obj_banana = Banana()

# obj_fruit.type()
# obj_fruit.colour()

# obj_apple.type()
# obj_apple.colour()

# obj_banana.type()
# obj_banana.colour()

class tv:
    def __init__(self,screen,brand,price):
        self.screen = screen
        self.brand = brand
        self.price = price

    def show_tv_details(self):
        print("Size of screen ", self.screen)
        print("Brand of tv ", self.brand)
        print("Price of tv ", self.price)

t1 = tv("32 inch", "samsung", 20000)
t1.show_tv_details()  






























