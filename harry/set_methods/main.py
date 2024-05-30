# I. union() and update(): the union() and update() are present in the two sets. The union() method returns a new set whereas update() method adds item into the existing set from another set. 

cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Kathmandu", "Madrid", "Seoul"}

print(cities1.union(cities2))
# cities1.update(cities2)
# print(cities1, cities2)

# The intersection() and intersection_update() methods prints only items that are similar to both the sets. The intersection() method returns a new set whereas intersection_update() method updates into the existing set from another set.


print(cities1.intersection(cities2))

# symetric_difference
print(cities1.symmetric_difference(cities2))

# difference
print(cities1.difference(cities2))



# Set methods

# isdisjoint(): checks if items of given set are present in another set. returns false if iterms are present, else returns true
print(cities1.isdisjoint(cities2))

# issuperset(): checks if all the items of a particular set are present in the original set. returns boolean
cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Kathmandu"}
print(cities1.issuperset(cities2))
cities3 = {"Tokyo", "Delhi"}
print(cities1.issuperset(cities3))

# issubset(): checks if all the items of the original set are present in the particular set.returns boolean
print(cities3.issubset(cities1))

# add(): add a single item to the set 
cities1.add("Helsinki")
print(cities1)

# update(): add more then one item, simplay create another set or any other iterable object(list, tuple, dictionary), and use the update() method to add it into the existing set.
cities1.update(cities2)
print(cities1)


# remove()/ discard(): remove raises an error, whereas discard() does not 
cities1.remove("Delhi")
print(cities1)

# pop(): removes the last item of the set but the catch is that we don't know which item gets popped as sets are unordered

# del : it is a keyword which deletes the set entirely
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities
# print(cities)

# clear(): clears all items in the set and prints an empty set
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear();
print(cities)
