# a = ["apple", "banana", "mango", "banana", "graps", "kiwi"]
# print(a)

# fruit= ["apple", "banana", "mango", "banana", "graps", "kiwi"]
# print(fruit.count("banana"))


# fruit= ["apple", "banana", "mango", "banana", "graps", "kiwi"]
# print(fruit.reverse())
# print(fruit)


# fruit = ["apple", "banana", "mango", "banana", "graps", "kiwi"]
# fruit.append("grape")
# print(fruit)


# fruit= ["apple", "banana", "mango", "banana", "graps", "kiwi"]
# fruit.pop()
# print(fruit)

# Using Lists as Stacks
# The list methods make it very easy to use a list as a stack, where the last element added is the first element
# retrieved (“last-in, first-out”). To add an item to the top of the stack, use append(). To retrieve an item from the top
# of the stack, use pop() without an explicit index.


# stack = [3,4,5,6]
# stack.append(8)
# stack.append(9)
# print(stack)


# stack = [3,4,5,6,7]
# stack.pop()
# print(stack)


# stack = [3,4,5,6]
# stack.pop()
# print(stack)

# stack = [3,4,5,]
# stack.pop()
# print(stack)


# Using Lists as Queues.
# It is also possible to use a list as a queue, where the first element added is the first element retrieved
# (“first-in, first-out”); however, lists are not efficient for this purpose. While appends and pops from the end of
# list are fast, doing inserts or pops from the beginning of a list is slow (because all of the other elements have
# to be shifted by one).



# sea_creatures = ['shark', 'cuttlefish', 'squid', 'mantis shrimp', 'anemone']
# print(sea_creatures)



# sea_creatures = ['shark', 'cuttlefish', 'squid', 'mantis shrimp', 'anemone']
# # print(sea_creatures[0])
# # print(sea_creatures[1])
# # print(sea_creatures[2])
# # print(sea_creatures[3])
# # print(sea_creatures[4])
#
#
# print(sea_creatures[-1])
# print(sea_creatures[-2])
# print(sea_creatures[-3])
# print(sea_creatures[-4])
# print(sea_creatures[-5])
#
# print("Sam is a ", sea_creatures[-5] )



# sea_creatures = ['shark', 'cuttlefish', 'squid', 'mantis shrimp', 'anemone']
# sea_creatures[1] = "octopus"
# print(sea_creatures)


# sea_creatures = ['shark', 'cuttlefish', 'squid', 'mantis shrimp', 'anemone']
# sea_creatures[-3] = "starfish"
# print(sea_creatures)


# Slicing Lists
# We can also call out a few items from the list. Let’s say we would like to just print the middle items of sea_creatures
# we can do so by creating a slice. With slices, we can call multiple values by creating a range of index numbers
# separated by a colon [x:y]:

#
# sea_creatures = ['shark', 'cuttlefish', 'squid', 'mantis shrimp', 'anemone']
# sea_creatures[0:4]
# print(sea_creatures)


# If we want to include either end of the list, we can omit one of the numbers in the list[x:y] syntax. For example, if
#     we want to print the first 3 items of the list


# sea_creatures = ['shark', 'cuttlefish', 'squid', 'mantis shrimp', 'anemone']
# print(sea_creatures[:3])
#
#
# sea_creatures = ['shark', 'cuttlefish', 'squid', 'mantis shrimp', 'anemone']
# print(sea_creatures[2:])


# One last parameter that we can use with slicing is called stride, which refers to how many items to move forward after
# the first item is retrieved from the list.

# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
#
# # print(numbers[1:11:2])
# print(numbers[::3])


# Modifying Lists with Operators
# Operators can be used to make modifications to lists. We’ll look at using the + and * operators and their compound forms
# += and *=.

































