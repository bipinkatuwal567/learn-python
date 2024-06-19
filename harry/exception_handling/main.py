# try... except blocks are used to handle errors and exceptions. The code in try block runs when there is no error. If the try block catches the error, then the except block is executed.



try: 
    num = int(input("Enter a number : "))
    print(f"Multiplication table of {num} is :")
    for i in range(1, 11): 
        print(f"{num} x {i} = {num*i}")
except Exception as e: 
    print(e)

print("Some lines of code")
print("End of program")
