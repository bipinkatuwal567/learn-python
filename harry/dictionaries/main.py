# Dictionaries are ordered collection of data items. They store multiple items in a single variable. Dictionary  items are key-value pairs that are separated by commas and enclodes within curly brackets {}.

info = {"name": "bipin", "age": 22, "eligible": True}
# print(info)

# 1. Accessing single values: 
# print(info['name'])
# print(info.get('name')) # returns none if there is error

# for key in info.keys():
#     print(info[key])

# 2. Accessing multiple values: 
# print(info.values())

# 3. Accessing keys: 
# print(int.keys())

# 4. Accessing key-value pairs: 
# print(info.items())

for key, value in info.items(): 
    print(key, value)
