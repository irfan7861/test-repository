#function
# def func1():
#     print("I am learning python function")
# func1()


# def my_function(fname):
#     print(fname + "Refsnes")
#
# my_function("Email")

# def square(x):
#     print(x * x)
# # print(square(4))
# square(4)


# def square(x):
#     return x*x
# print(square(4))




#
# def multiply(x,y):
#     print(x*y)
#
# multiply(2,6)
#
#
#
# def plus(x,y,z):
#     print(x+y+z)
# plus(9,8,6)
#
#
# def multiply(x,y):
#     print("Value of x ", x)
#     print("Value of y ", y)
#
#     return x*y
#
# print(multiply(5,6))


class Tv:
    def __init__(self,price,color):
        self.price = price
        self.color = color
    def show_tv_details(self):
        print("Price of tv", self.price)
        print("Color of tv", self.color)
t1 = Tv(30000,"red")
t1.show_tv_details()















# marks= [87.76,87,98]
# percentage1= (sum(marks)/400)*100
#
# marks2= [91.25,56,47]
# percentage2= (sum(marks)/400)*100
#
# print(percentage1,percentage2)
#how function works

#
# def percent(marks):
#     p=((marks[0] + marks[1] + marks[2] + marks[3])/400)*100
#     return p
# marks1= [87, 76, 87, 98]
# percentage1= percent(marks1)
#
# marks2= [91, 25, 56, 47]
# percentage2= percent(marks2)
# print(percentage1,percentage2)

#exaples

# def greet(name):
#     print("Good day, "+ name)
#
# greet("irfan")

# Types of function
# 1. Built in function - Already present in python exp- len,print etc
# 2. User defines functions - Defined by user.

#examples
# def greet(name):
#      print("Good day, "+ name)
# def mysum(num1, num2):
#     return num1 + num2
# greet("irfan")
# s= mysum(6, 32)
# print(s)

#default arguments

# def greet(name="smaeer"):
#     print("Good day, " + name)
#
# greet("irfan")
# greet( )

#Recursion

#n!=1 * 2 * 3 * 4...*n
# n=4
# product=1
# for i in range(n):
#     product = product * (i+1)
# print(product)
#
# def factorial_iter(n):
#     product = 1
#     for i in range(n):
#         product = product * (i+1)
#     return product

# print(factorial_iter(5))

#n!=[1 * 2 * 3 * 4...*n-1] *n
#n!= n * (n-1)!


# def factorial_recursive(n):
#     if n == 1 or n==0:
#         return 1
#     return n * factorial_recursive(n-1)
#
# f = factorial_recursive(6)
# print(f)

# def xyz():
#     print("i am recursion")
#
# xyz()
#
# def xyz1():
#     print("indirect recursion")
#     xyz()
#
# xyz1()


#global

# i = 0
#
# def myfun():
#     global i
#     i=i+1
#     print("My function", i)
#     myfun()
#
# myfun()

# class Person():
#     def __init__(self,name,age,height,weight):
#         self.name = name
#         self.age = age
#         self.height = height
#         self.weight = weight
#
# obj1 = Person("irfan",25,172,80)
#
# # print(obj1.name)
# # print(obj1.age)
# # print(obj1.height)
# # print(obj1.weight)
# print(obj1.name,obj1.age,obj1.height,obj1.weight)


# class mobile:
#     def __init__(self):
#         self.model = 'realmex'
#     def show_details(self):
#         print("model", self.model)
# realme = mobile()
# # realme.show_details()
# realme.model = 'realme pro'
# realme.show_details()



# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
#
# print(factorial(4))


# Recursive reverse a string
# def reverseStr(s):
#     if len(s) == 1:
#         return s[0]
#     else:
#         return reverseStr(s[1:]) + s[0]
# print(reverseStr("irfan"))

# Iterative sum
# def iterativeSum(l):
#     total = 0
#     for e in l:
#         total += e
#     return total

