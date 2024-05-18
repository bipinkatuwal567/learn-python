# There are four types of arguments that we can provide in a functions: 

# Default Arguments
# Keyword Arguments
# Variable Length Arguments
# Required Arguments

# Default Arguments
def name(fname, mname="D.", lname="Katuwal"): 
    print("Hello", fname, mname, lname)
    
name("Bipin")

# Keyword Arguments
# We can provide arguments with key = value, this way the interpreter recognized the arguments by the parameter name. Hence, the order in which the arguments are passed does not matter.

def name(fname, mname, lname): 
    print("Hello", fname, mname, lname)
    
name(lname="Katuwal", fname="bipin", mname="kumar")

# Required Arguments
# In case we don't pass the arguments with a key = value syntax, then it is necessary to pass the arguments in the correct positional order and the number of arguments passed should match with actual function definition. 

# Variable-length Arguments
# Sometimes we may need to pass more arguments than those defined in the actual function. This can be done using variable length arguments.
# There are two ways to achieve this: 

# Arbitrary Arguments: While creating a function, pass a * before parameter name while defining the function. The function accesses the arguments by processing them in the form of tuple.

def name(*name): 
    for value in name:
        print(value, end=",")
name("Bipin", "Forest", "Roshan")

# Keyword Arbitrary Arguments: While creating a function, pass a * before the parameter name while defining the function. The function access the arguments by processing them in the form dictionary.

def name(**name): 
    print("\nHello,", name["fname"], name["mname"], name["lname"])

name(fname="Bipin", mname="Kumar", lname="Katuwal")