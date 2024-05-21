# Manipulating Tuples
# Tuples are immutable, hence if you want to add, remove or change tuple items, then first you must convert the tuple to a list. Then perform operation on that list and covert it back to tuple.

countries = ("Nepal", "Spain", "Italy", "India", "England", "Germany")

print(countries)

tempCountries = list(countries)
tempCountries.append("Russia")
tempCountries.pop(5)
tempCountries[3] = "Finland"
countries = tuple(tempCountries)

print(countries)

# Thus, we convert the tuple to a list, manipulate items of the list using list methods, then convert list back to a tuple. 

# However, we can directly concatenate two tuples without converting them to list

countries = ("Pakistan", "Afghanistan", "Bangladesh", "Shrilanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)

# count() : The count() method of Tuple returns the number of times the given element appears in the tuple.
tuple1 = (0,1,2,3,2,3,1,3,2,3,5,3)
print(tuple1.count(3))

# index(): The index() method returns the first occurence of the given element from the tuple
print(tuple1.index(2))