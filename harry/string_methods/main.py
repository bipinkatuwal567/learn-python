# String are immutable
a = "forest"

# upper() method converts string to upper case
print(a.upper())

# upper() method converts string to upper case
print(a.lower())

# rstrip() method removes any trailing characters
b = "hello !!!!!"
print(b.rstrip("!"))

# replace() method replaces all occurences of a string with a another string
print(b.replace("hello", "hi"))

# split() method splits the given string at the specified instance and returns the separated strings as list items
print(b.split(" "))

# capitalize() method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase. 
capital = "hello my name iS bIpiN bipin Bipin"
print(capital.capitalize())

# count() method returns the number of times the given value has occured within the given string
print(capital.count("bipin"))

#  endswith() method checks if the string ends with a given value. If yes then return True, else return False.
str1 = "Welcome to the Python !!!"
print(str1.endswith("!!!"))
# We can also check for a value in-between the string by providing start and end index positions
print(str1.endswith("to", 4, 10))

# isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns false.
str1 = "WelcomeToThePython"
print(str1.isalnum())

# isalpha() method returns True if only if the entire string only consists of A-Z, a-z. If any other characters or punctuations or number(0-9) are present, then it reutrns false
str1 = "Welcome"
print(str1.isalpha())




# islower() method returns True if all the characters in the string are lower case, else it returns False
str1 = "hello world"
print(str1.islower())
