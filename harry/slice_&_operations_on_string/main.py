# Length of a String
# We can find the length of a string using len() function

usernames = "Forest,Bipin"
print(len(usernames))

# Slicing
# Specify the start index and the end index, separated by a colon, to return a part of the string.
# The first character has index 0.

a = "Hello, World!"
print(a[2:5]) # Prints llo (including 2 but on 5)

# Slice from the start
print(a[:5]) # Hello

# Slice to the end
print(a[0:]) # Hello, World!

# Negative Indexing
print(a[-5:-2]) # orl

# Quick Quiz
nm= "Harry"
print(nm[-4:-2])
