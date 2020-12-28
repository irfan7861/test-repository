# fruits = ["Apple", "banana", "cherry"]
# for x in fruits:
#     print(x)
#
# #Looping Through a String
# for x in "banana" :
#     print(x)

sharks = ["hammerhead", "great white", "dogfish", "frilled", "bullhead", "requiem"]
print(sharks[0:4])
# for x in sharks:
#    print(x)
# thisis = 'then'
# print(type(thisis))


# The break Statement
# Exit the loop when x is "banana":
# fruits = ["banana", "banana", "cherry"]
# for x in fruits:
#     print(x)
#     if x == "banana":
#         break
# Exit the loop when x is "banana", but this time the break comes before the print
# fruits = ["banana", "banana", "cherry"]
# for x in fruits:
#     if x == "banana":
#         break
# print(x)

# The continue Statement
# With the continue statement we can stop the current iteration of the loop, and continue with the next:
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     if x == "banana":
#         continue
# print(x)

# The range() Function
# To loop through a set of code a specified number of times, we can use the range() function,
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number

# for x in range(8):
#     print(x)

# Note that range(6) is not the values of 0 to 6, but the values 0 to 5
# for x in range(2, 6):
#     print(x)

# note-The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):

# Increment the sequence with 3 (default is 1):
# for x in range(2, 30, 3):
#     print(x)

# Else in For Loop
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
# for x in range(6):
#     print(x)
# else:
#     print("finally finished")

# The else block will NOT be executed if the loop is stopped by a break statement.
# Break the loop when x is 3, and see what happens with the else block:
# for x in range(6):
#     if x == 3: break
#     print(x)
# else:
#     print("finally finished")
#



# Nested Loops
# A nested loop is a loop inside a loop.
#
# The "inner loop" will be executed one time for each iteration of the "outer loop":
#
# adj = ["red", "green", "blue"]
# fruits = ["apple", "banana", "cherry"]

# for x in adj:
#     for y in fruits:
#         print(x, y)

# The pass Statement
# for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.

# for x in [0, 1, 2]:
#     pass


# n = 8
# for i in range(4, n):
#     print(i)
#
# n = 50
# for i in range(45, n):
#     print(i)

# print("list Iteration")
# l = ["geeks", "for", "geeks" ]
# for i in l:
#     print(i, end=',')

# Iterating over a tuple (immutable)
# t = ("geeks", "here", "geeks")
# for i in t:
#     print(i, end=',')

# Iterating over a String
# t = "geeks"
# for i in t:
#     print(i, end=',')


# Iterating over dictionary
# d = dict()
# d["xyz"] = 123
# d["abc"] = 345
# for i in d:
#     print(i)
#     print('%s %d' %(i, d[i]))

#not understand this

# Iterating by index
#
# list = ["geeks", "here", "geeks"]
# for index in range(len(list)):
#     print (list[index])

# combining else with for


# list = ["geeks", "here", "geeks"]
# for index in range(len(list)):
#     print (list[index], end=',')
# else:
#     print ("Inside Else Block" )

# nested for loops in Python
# for i in range(1, 5):
#     for j in range (i):
#         print(i, end=' ')
#     print()
#
# for i in range(1, 50,9):
#     for j in range (1,20,2):
#         print(i, j,end=' ')
#     print()
# Continue Statement: It returns the control to the beginning of the loop.
# for letter in "irfanshaque":
#     if letter == 'e' or letter == 's':
#         continue
#     print ("current letter:", letter)
#     var = 10

# for letter in "irfanshaque":
#     if letter == 'i' or letter == 'h':
#         continue
#     print ("current letter:", letter)

# Break Statement: It brings control out of the loop
# for letter in "irfanshaque":
#     if letter == 'f' or letter == 'h':
#         break
#     print("current letter :", letter)

# A simple for loop example
# fruits = ["apple", "orange", "kiwi"]
# for i in fruits:
#     print(i)

#With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

#adj = ["red", "green", "blue"],["apple", 123455, "banana"],("sweet", "salty", "bitter")

# for x in adj:
#     print(x, end="")












# Iterating over dictionary
# d = dict()
# d["xyz"] = 123
# d["abc"] = 345
# for i in d:
#     print(i)
#     print('%s %d' %(i, d[i]))






















































