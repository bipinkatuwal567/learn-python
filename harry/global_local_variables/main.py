# A local variable is a variable that is defined within a function and is only accessible within that function. It is created when the function is called and is destroyed when the function returns. 

# On the other hand, a global variable is a variable that is defined outside of a function and is accessible from within any function in your code. 

x = 4 
print(x)

def hello(): 
    global x
    x = 5
    print(f"The local is {x}")
    print("Hello stranger")

print(f"The global x is {x}")
hello()
print(f"The global x is {x}")