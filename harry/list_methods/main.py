# List Methods

# Append Items: To add an item to the end of the list, use the append() method:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# Insert Items: To insert a list item at a specified index, use the insert() method
thislist.insert(1, "grape")
print(thislist)

# Sort : This method sorts the list in ascending orer. This original is updated
colors = ["voilet", "indigo", "blue", "green"]
colors.sort()
print(colors)

num = [11, 100, 45, 66, 6, 98]
num.sort();
# num.sort(reverse=True); This reverse the list
# num.reverse();
print(num)

# copy: Returns copy of the list. This can be done to perfomr operations on the list without modifying the origina list.
newList = colors.copy()
newList.insert(0, "red")
print(colors)
print(newList)

# extend: This method adds an entire list or any other collection datatype (set, tuple, dictionary) to the existing list.
a = [45,67,89,90]
b = [122,134,546,754]

# a.extend(b)
# print(a)

# Concatenating two lists:
print(a + b)
