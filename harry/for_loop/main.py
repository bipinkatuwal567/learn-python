# for loops can iterate over a sequence of iterable objects in python.

name = "forest"

for value in name: 
    print(value, end=", ")
    
colors = ["Red", "Green", "Blue", "Yellow"]

for color in colors: 
    print(color, end=", ")
    
for i in range(1, 20, 2):
    print(i)