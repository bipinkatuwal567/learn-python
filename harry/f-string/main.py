# String formatting 
letter = "Hey my name is {1} and I am from {0}"
country = "Nepal"
name = "Bipin"

print(letter.format(country, name))

# F-string allows you to format selected parts of a string.
# To specify a string as an f-string, simply put and f in front of the string literal.
print(f"Hey my name is {name}. I am from {country}")

# If i want to user curly brackets then: 
print(f"Hey my name is {{name}}. I am from {{country}}")
