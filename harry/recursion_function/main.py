# Recursion is the process of defining something in terms of itself.

def fact(n): 
    if n ==1 or n == 0: return 1
    return (n * fact(n-1))

# print(fact(5))

# Fibonacci
def fib(n): 
    if n <= 1:
        return n
    else: 
        return fib(n-1) + fib(n-2)

for i in range(10): 
    print(fib(i))