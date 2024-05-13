# Strings in python are surrounded by either single quotation marks, or double quotation marks.

username = "forest"
print(username)

# We can use quotes inside a string, as long as they don't match the quotes surrounding the string
print("Hello, I'm Bipin Katuwal!")

# Multiline Strings
# We can assign a multiline string to a variable by using three quotes:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
"""
print(a);

# Accessing Characters in a String
print(username[0]) # It will print f

# Looping through the string
for charater in username:
    print(charater);

# Check String
# To check if a certain phrase or character is present in a string, we can use the keyword in.

txt = "The best things in life are free!"
print("free" in txt) # It will print true 