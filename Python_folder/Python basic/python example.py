# #Python Program to Print Hello world.
#
# print("hello world")
#
# #Python Program to Add Two Numbers.
#
# a = 5
# b = 10
# sum = a+b
# print("The sum of a and b is", sum)
#
# #Python Program to Find the Square Root.
#
# num = 2
# num_sqrt = num ** 0.5
# print(num_sqrt)
#
# #Python Program to Calculate the Area of a Triangle
#
# a = 5
# b = 6
# c = 7
# s = (a+b+c)
# sa = s/2
# area = (sa*(sa-a)*(sa-b)*(sa-c)) ** 0.5
# print(area)
#
#
# #Python Program to Solve Quadratic Equation
#
# #Python Program to Swap Two Variables
#
# x = 5
# y = 10
#
# temp = x
# x = y
# y = temp
# print(x, y)
#
# #Python Program to Generate a Random Number
# import random
# print(random.randint(0,10))
#
# Python Program to Convert Kilometers to Miles
# km = 3.5
# conversion = km*0.62
# print("3.5 km is equal to =", conversion , "miles")
#
# #Python Program to Convert Celsius To Fahrenheit
#
# celcious = 37.5
# conversion = celcious*9/5+32
# print("37.5 Celsius converted to Fahrenheit=", + conversion )
#
# #Python Program to Check if a Number is Positive, Negative or 0
# #
# num = 0
#
# if num > 0:
#     print("positive number")
# elif num == 0:
#     print("zero")
# else:
#     print("negative number")
#
# # Python Program to Check if a Number is Odd or Even
# user = int(input("Please enter a number"))
#
# if (user % 2) == 0:
#     print("Its a even number")
# else:
#     print("Its a odd number")
#
#
# #Python Program to Check Leap Year
#
# user = int(input("Eneter a year"))
#
# if (user % 4) == 0:
#     if (user % 100) == 0:
#         if (user % 400) == 0:
#             print("Its a leap year")
# else:
#     print("Its no a leap yaer")
#
#
# # Python program to find the largest number among the three input numbers
# a = int(input("Please enter anumber"))
# b = int(input("Please enter anumber"))
# c = int(input("Please enter anumber"))
#
# if (a >= b) and (a >= c):
#     print("Largest Number is ", a)
# elif (b >= a) and (b >= c):
#     print("Largest Number is ", b)
# else:
#     print("Largest Number is ", c)
#
# # Program to check if a number is prime or not
#
# a = 7
#
# if a > 1:
#     for i in range(2,a):
#         if (a % 1) == 0:
#             print("Its note a prime number")
#
# else:
#     print("Its a prime number")
#
# # Python program to display all the prime numbers within an interval
# a = 900
# b = 1000
#
# print("All prime numbers between 900 To 1000 are-")
# for i in range(a, b+1):
#     if i > 1:
#         for y in range(2, i):
#             if (i % y) == 0:
#                 break
#         else:
#             print(i)
#
# # Python Program to Find the Factorial of a Number
#
#
# n = 10
# fact = 1
# for i in range(1,n+1):
#     fact = fact * i
#
# print("the factorial of 13 is:", end="")
# print(fact)
#
# # Python Program to Display the multiplication Table
# table = int(input("entr a number"))
#
# for i in range(1, 11):
#     print(table, "X", i, "=", table*i)

# Python Program to Print the Fibonacci sequence
#
# def fiboIter(n):
#     pass
#
# def fiboRecur(n):
#     if n==0:
#         return 0
#     elif(n==1):
#             return 1
#     else:
#         return fiboRecur(n-1) + fiboRecur(n-2)
#
#
#
# if __name__ == '__main__':
#     num =int(input("Enter a number"))
#     print(f"Using recursion value of fib({num}) is {fiboRecur(num)}")

# Python Program to Check Armstrong Number
# num = int(input("Enter a number"))
# orig = num
# sum = 0
#
# while num > 0:
#     sum = sum + (num%10)*(num%10)*(num%10)
#     num = num//10
#
# if orig == sum:
#      print("is armstrong number")
# else:
#      print("is not armstrong number")
#
# Python Program to Check Armstrong Number in interval

# lower = int(input("enter a number"))
# upper = int(input("enter a number"))
#
# for num in range(lower,upper+1):
#     order = len(str(num))
#
# sum = 0
# orig = num
#
# while orig > 0:
#     sum = sum + (orig%10)*(orig%10)*(orig%10)
#     orig = orig//10
#
# if orig == sum:
#      print("is armstrong number")
# else:
#      print("is not armstrong number")



#Python Program to Find the Sum of Natural Numbers






















































