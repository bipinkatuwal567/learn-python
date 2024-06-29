# f = open("test.txt", "r")
# text = f.read()
# print(text)
# f.close()

# The "with" statement
# Alternatively, you can use the with statement to automatically close the file after you are done with it. 

with open("test.txt", "a") as f: 
    f.write("Hey i am text \n")