num = int(input("Enter a number between 1 to 9 : "))

if(num < 1 or num > 9): 
    raise("Number is not between 1 to 9")
else: 
    print(f"{num} is a number you entered")