# a function without a name is called anonymous function.It is also known as lambda function.
#syntex:-

# lambda argument_list : Expression

# lambda x,y : x+y

# sum = lambda x: x+1
#
# print(sum(5))
#
# multiply = lambda x: x*5
# print(multiply(6))
#
# add = lambda x,y: x+y
# print(add(5,4))

#function and lambda gives same output:
#Normal function
# def name(x):
#     print(x)
# print(name(5))
#
# #Lambda Function
# show = lambda x: print(x)
# show(5)


# add_sub = lambda x,y: (x+y, x-y)
# print(add_sub(4,5))



add_sub = lambda x,y: (x+y, x-y)
a,z = add_sub(4,5)
print(a)
print(z)




add = lambda x,y=3: x+y
print(add(5))



