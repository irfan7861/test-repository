#dictionary is nothing but key value pairs
#
# d={}
# print(type(d))
# d2= {"irfan":"burger", "shahir":"fish", "gourav":"roti"}
#
# d3= {"name": "shahir", "food": "fish", "location": "delhi"}
# #d4= {{"name": "shahir", "food": "fish", "location": "delhi"},{"name": "sameer", "food": "chicken", "location": "up"}}
# print(d3)
#


# print(d2)
# #
# print(d2["shahir"])
# # add in dictionary

# d3["name"]= "junk food"
# # d2["amir"]= "kabab"
# print(d3)
#
#
# # Delete in dictionary

# del d2["amir"]
# print(d2)

# Copy in dictionary

# d2= {"irfan":"burger", "shahir":"fish", "gourav":"roti"}
# # print(d2.copy())
# # Update in dictionary
#
#
# d2.update({"rahul":"maggie"})
# print(d2)

# mydict = dict(("name", "shahir", "food", "fish", "location", "delhi"),("name", "sameer", "food", "chicken", "location", "up"))
# print(mydict)

# thisdict= {"brand": "ford",
#            "model": "mustang",
#            "year": 1964}
# print(thisdict)

# Print the "brand" value of the dictionary:

# thisdict= {"brand": "ford",
#            "model": "mustang",
#            "year": 1964}
# print(thisdict["brand"])

# Duplicate values will overwrite existing values:
# thisdict= {"brand": "ford",
#            "model": "mustang",
#            "year": 1964,
#            "year": 2020}
# print(thisdict)

# Dictionary Length

# thisdict= {"brand": "ford",
#            "model": "mustang",
#            "tyre": "apollo"}
# print(len(thisdict))

# The values in dictionary items can be of any data type:


# thisdict= {"brand": "ford",
#            "electric": "False",
#            "year": "2020",
#            "colour": ["red", "white", "blue"]}
# print((thisdict))


# dictionary with integer keys

# my_dict = {1: "apple", 2: "ball"}
# print(my_dict)
# print(my_dict[1])

# Removing elements from a dictionary

# squares = {1: 1, 2: 4, 3: 9, 4:16, 5:25}
#
# print(squares)
# print(squares.pop(4))
# print(squares)

# Dictionary Comprehension
# squares = {x: x*x for x in range(6)}
# print(squares)

# This code is equivalent to
# squares = {}
# for x in range(6):
#     squares[x] = x*x
# print(squares)

# Dictionary Comprehension with if conditional
# oddsquares = {x: x*x for x in range(11) if x % 2 == 1}

# print(oddsquares)

# Membership Test for Dictionary

# squares = {1:1, 3:9, 5:25, 7:49, 9:81}
# print(squares)
# print(1 in squares)
# print(2 in squares)

# Iterating through a Dictionary
squares = {1:1, 3:9, 5:25, 7:49, 9:81}
for i in squares:
    print(squares[i])















