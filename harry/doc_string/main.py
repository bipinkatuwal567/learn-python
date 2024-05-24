# docstrings are the string literals that appear right after the definition of a function, method, class, or module.
# There is difference between comment and docstrings

def square(n): 
    '''Takes in a numbern, returns the square of n'''
    print(n ** 2)

square(5)
print(square.__doc__)