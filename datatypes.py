# What is a Data Type?

# A data type tells Python what kind of data a variable contains.

name = "Salaar"
age = 23;
is_student = True

# access characters
print(name[0])
print(name[2])

print(type(name))
print(age, type(age))

# Main Python datatypes

# string --> str
# example

brand_name = "Guchi"
student_name = "Ijaz"

# integer --> int
# example

age = 45;
print(age)


# float used for decimel numbers

number = 56.8
print(number)

# bool used for true false

is_loggedIn = True
is_passed = False
print(is_passed)

# list is used for ordered collection
# example --> [7,8,9,3]
# we use square brackets
# lists are used to store values
# lists are mutable

items = [3,9,93,4,5,67,23]
print(items)

# tuple is used for fixed collection
# tuples are immutable

example = (1,2,3,4,5)
print(example)

# set is used for unique numbers or for unique values.
# Duplicates are removed.

set_example = {67,9,5,9,2.3,6,1,6}
print(set_example)

# dictionary is used for key-value data
# Dictionary is extremely important, especially for backend development and APIs.

user = {
    "name": "amjad",
    "age": 78,
    "role": "Software Engineer"
}

print(user)

# NoneType
# There is currently no value.

result = None

print(result)
print(type(result))