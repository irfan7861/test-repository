# Set
# Sets are used to store multiple items in a single variable.
#
# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and
# Dictionary, all with different qualities and usage.
#
# A set is a collection which is both unordered and unindexed.
#
# Sets are written with curly brackets.

# set1 = {1,2,3,4,5,6,7,47,8,8,8,8,8}
# print(set1)
# print(type(set1))

# set2 = {3,4,5,6,45,47,9}
# # print(set1.union(set2))
# # print(set1.intersection(set2))
# print(set1.difference(set2))

# Note: Sets are unordered, so you cannot be sure in which order the items will appear.
# Set Items
# Set items are unordered, unchangeable, and do not allow duplicate values.
#
# Unordered
# Unordered means that the items in a set do not have a defined order.
#
# Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
#
# Unchangeable
# Sets are unchangeable, meaning that we cannot change the items after the set has been created.
#
# Once a set is created, you cannot change its items, but you can add new items.

# Duplicates Not Allowed
# Sets cannot have two items with the same value.

# set1 = {"apple", "banana", "cherry"}
# set2 = {1, 5, 7, 9, 3}
# set3 = {True, False, False}
#
# print(type(set1))
# print(type(set2))
# print(type(set3))


# The set() Constructor
# It is also possible to use the set() constructor to make a set.

# set1 = set(("apple", "mango", "kiwi", "banana"))
# print(set1)
# print(type(set1))



# Add Items
# Once a set is created, you cannot change its items, but you can add new items.
#
# To add one item to a set use the add() method.

# add1 = {"apple", "banana", "cherry"}
#
# add1.add("orange")
#
# print(add1)

# Add Sets
# To add items from another set into the current set, use the update() method.

# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"}
#
# thisset.update(tropical)
#
# print(thisset)

# Remove Item
# To remove an item in a set, use the remove(), or the discard() method.
# thisset = {"apple", "banana", "cherry"}
#
# thisset.remove("cherry")
# print(thisset)


# The clear() method empties the set:

# thisset = {"apple", "banana", "cherry"}
# thisset.clear()
# print(thisset)


# Loop through the set, and print the values:
#
# thisset = {"apple", "banana", "cherry"}
#
# for x in thisset:
#   print(x)

# The union() method returns a new set with all items from both sets:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

# The update() method inserts the items in set2 into set1:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

# Keep the items that exist in both set x, and set y:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)











































