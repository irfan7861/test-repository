import re

# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)

# if x:
#   print("YES! We have a match!")
# else:
#   print("No match")


# Function	Description
# findall	-  Returns a list containing all matches
# search	 - Returns a Match object if there is a match anywhere in the string
# split	 - Returns a list where the string has been split at each match
# sub	    -   Replaces one or many matches with a string

# txt = "The rain in Spain"

#Find all lower case characters alphabetically between "a" and "m":

# x = re.findall("[a-m]", txt)
# print(x)


txt = "The rain in Spain"

#Check if the string has any a, r, or n characters:

x = re.findall("[arn]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


txt = "The rain in Spain"

#Check if the string has any characters between a and n:

x = re.findall("[a-n]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


z = "This is not america"
x = re.search("^This.*america$", z)
if x:
    print("Yes we have a match")
else:
    print("No match")    


#Return a list containing every occurrence of "in":
txt = "The rain in Spain"
x = re.findall("in", txt)
print(x)

a = "once upon a time in maxico"
x = re.findall("o", a)
print(x)




















