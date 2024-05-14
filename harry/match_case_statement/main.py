x = input("Enter the value of x: ")

match x: 
    case "1": 
        print(x, "is number one")
    case "10": 
        print(x, "is number ten")
    case "100": 
        print(x, "is number hundred")
    case _:
        print(x, "has no place in match")