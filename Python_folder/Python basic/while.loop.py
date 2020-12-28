# With the while loop we can execute a set of statements as long as a condition is true.

# i = 1
# while i<= 6:
#     print(i)
#     i +=1

# i++
# i+1
# i+2
# i+4...

# The while loop requires relevant variables to be ready, in this example we need to define an indexing variable, i, which we set to 1.

# The break Statement
# With the break statement we can stop the loop even if the while condition is true:
#  exit the loop when i is 3

# for i in range(11, 20,4):
#     print(i+1, end=',')


# The continue Statement
# With the continue statement we can stop the current iteration, and continue with the next:

# i = 0
# while i < 6:
#     i += 1
#     if i == 3:
#         continue
#     print(i)

# The else Statement

# i = 1
# while i < 6:
#     print(i)
#     i += 1
# else:
#     print("i is no longer less than 6")

# While loops are really similar to if statements.

# its_raining = True
# while its_raining:
#     print("Oh crap, it's raining!")
# print("it's not raining anymore.")



#while loop with conditional statements if else

# x = 1
# while x <= 5:
#     print(x)
#     if x == 3:
#         break
#     x = x+1


# x = 1
# while x <= 5:
#     if x == 3:
#         x = x+1
#         continue
#     else:
#         print(x)
#         x = x + 1

# Infinite while loop
#
# i = 1
#
# while i < 10:
#     print(i)
#     i += 1
#
# dates = [1982, 1980, 1973, 2000]
#
# i = 0;
# year = 0
# while (year != 1973):
#     year = dates[i]
#     i = i + 1
#     print(year)
#
# print("it took ", i, "repetitions to get out of loop")
#
#
# count = 0
# while (count <= 3):
#     count = count+1
#     print("hello")

# count=0
# while (count <= 3):
#     count = count + 1
#     print("this is your turn")
# else:
#     print("In else block")



# count = 0
# while (count == 0): print("hello world")


# Note: It is suggested not to use this type of loops as it is a never ending infinite loop where the condition is always
# true and you have to forcefully terminate the compiler.


# While Loop
# We use the reserved word while to make a while loop. It is used to execute a block of statements repeatedly until a
# given condition is satisfied. When the condition becomes false, the lines of code after the loop will be continued to be executed.
# count = 0
# while count < 7:
#     print(count)
#     count = count + 3

# In the above while loop, the condition becomes false when count is 5. That is when the loop stops.
# If we are interested to run block of code once the condition is no longer true, we can use else.
count = 0
# while count < 7:
#     print(count)
#     count = count + 3
# # else:
# #     print(count)
# else:
#     print("ok")
#
# Break: We use break when we like to get out of or stop the loop.
# num = 0
# while num < 6:
#     print(num)
#     num = num + 1
#     if num == 5:
#         break
# Simply we can use while and range() function in python.
# x=1
# while x in range(1, 11):
#     print(x)
#     x = x + 1
#     if 1 == 9:
#         break


# x = 1
# while x in range(1, 20):
#     print(x)
#     x = x + 1
#     if x == 10:
#         break

# x = 1
# while x in range(1, 20):
#     print(x)
#     x = x + 1
#     if x == 10:
#         continue

# x = 1
# while x < 10:
#     print(x)
#     x = x + 1
#     if x == 5:
#         break
# With the while loop we can execute a set of statements as long as a condition is true.
# x = 1
# while x < 8:
#     print(x)
#     x = x + 1

###################################
# x = 1
# while x < 8:
#     print(x)
#     x = x + 1
#     if x == 8:
#         print("finish")
#
# password = ""
# while password != "irfan1995":
#     print("what is your password?")
#     password = input()





#
# password = ""
# while password != "irfan98989":
#     print("Please enter your password?")
#     password = (input())


a = 1
b = 2
while a < 0:
    while b < 1:
        print(a,b)








































































































