# Functions
# A function is a block of code that performs a specific task whenever it is called. 

# There are two types of functions: 
# 1. Buildt-in functions: min(), max(), print(), range(), type()
# 2. User-defined functions: userDefined

def calculateGmean(a, b): 
    print((a*b)/(a+b))

calculateGmean(9,8)

def findGreaterNumber(a, b): 
    if a > b: 
        print("A is greater")
    else: 
        print("B is greater")

findGreaterNumber(5, 7)
findGreaterNumber(7, 5)