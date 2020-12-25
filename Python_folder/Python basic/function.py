#function
# marks= [87.76,87,98]
# percentage1= (sum(marks)/400)*100
#
# marks2= [91.25,56,47]
# percentage2= (sum(marks)/400)*100
#
# print(percentage1,percentage2)
#how function works


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

# def factorial_iter(n):
#     product = 1
#     for i in range(n):
#         product = product * (i+1)
#     return product
#
# print(factorial_iter(5))

#n!=[1 * 2 * 3 * 4...*n-1] *n
#n!= n * (n-1)!


def factorial_recursive(n):
    if n == 1 or n==0:
        return 1
    return n * factorial_recursive(n-1)

f = factorial_recursive(6)
print(f)






