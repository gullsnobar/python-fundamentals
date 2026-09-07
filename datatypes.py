# ============================================================
# PYTHON DATA TYPES
# ============================================================
# A data type tells Python what kind of data a variable contains.
#
# Common Python data types:
#
# str       -> String
# int       -> Integer
# float     -> Decimal number
# bool      -> True or False
# list      -> Ordered, mutable collection
# tuple     -> Ordered, immutable collection
# set       -> Collection of unique values
# dict      -> Key-value pairs
# NoneType  -> No value
# ============================================================


# ============================================================
# 1. STRING -> str
# ============================================================
# A string is used to store text.
#
# Strings are written inside:
# "double quotes" or 'single quotes'


name = "Salaar"
brand_name = "Gucci"
student_name = "Ijaz"

print(name)
print(brand_name)
print(student_name)

print(type(name))


# ------------------------------------------------------------
# Access Characters in a String
# ------------------------------------------------------------
# We can access individual characters of a string using
# indexes.
#
# Python indexing starts from 0.
#
# Example:
# S a l a a r
# 0 1 2 3 4 5


print(name[0])  # S
print(name[2])  # l


# Negative indexing starts from the end.
#
# S a l a a r
# -6 -5 -4 -3 -2 -1

print(name[-1])  # r
print(name[-2])  # a


# ============================================================
# 2. INTEGER -> int
# ============================================================
# An integer is a whole number.
#
# Integers can be positive, negative, or zero.
#
# Examples:
# 10
# 25
# -5
# 0


age = 45
score = 100
temperature = -5

print(age)
print(type(age))


# ============================================================
# 3. FLOAT -> float
# ============================================================
# A float is a number that contains a decimal point.
#
# Examples:
# 10.5
# 3.14
# -2.5


number = 56.8
price = 99.99

print(number)
print(type(number))


# ============================================================
# 4. BOOLEAN -> bool
# ============================================================
# Boolean represents one of two values:
#
# True
# False
#
# Booleans are commonly used for conditions and status.


is_logged_in = True
is_passed = False

print(is_logged_in)
print(is_passed)

print(type(is_logged_in))


# ============================================================
# 5. LIST -> list
# ============================================================
# A list is used to store multiple values in an ordered
# collection.
#
# Lists are:
# - Ordered
# - Mutable (can be changed)
# - Can contain duplicate values
# - Can contain different data types
#
# Lists use square brackets []


items = [3, 9, 93, 4, 5, 67, 23]

print(items)
print(type(items))


# Access an item using its index.

print(items[0])  # 3
print(items[2])  # 93


# Lists are mutable, which means we can change their values.

items[0] = 100

print(items)


# Adding an item to a list:

items.append(50)

print(items)


# ============================================================
# 6. TUPLE -> tuple
# ============================================================
# A tuple is used to store multiple values in an ordered
# collection.
#
# Tuples are:
# - Ordered
# - Immutable (cannot be changed)
# - Can contain duplicate values
#
# Tuples usually use parentheses ()


example = (1, 2, 3, 4, 5)

print(example)
print(type(example))


# Access a tuple item using its index.

print(example[0])
print(example[2])


# Tuples are immutable.
# The following code would cause an error:
#
# example[0] = 100


# ============================================================
# 7. SET -> set
# ============================================================
# A set is used to store unique values.
#
# Sets:
# - Do not allow duplicate values
# - Are unordered
# - Are mutable
#
# Sets use curly brackets {}


set_example = {67, 9, 5, 9, 2.3, 6, 1, 6}

print(set_example)
print(type(set_example))


# Notice:
# 9 appears twice in the original set,
# but Python keeps only one 9.
#
# 6 also appears twice,
# but Python keeps only one 6.


# Adding a value to a set:

set_example.add(100)

print(set_example)


# ============================================================
# 8. DICTIONARY -> dict
# ============================================================
# A dictionary stores data in key-value pairs.
#
# Each key is connected to a value.
#
# Example:
#
# "name" -> "Amjad"
# "age"  -> 78
# "role" -> "Software Engineer"
#
# Dictionaries use curly brackets {}
#
# Dictionaries are very commonly used in backend development
# and APIs.


user = {
    "name": "Amjad",
    "age": 78,
    "role": "Software Engineer"
}

print(user)
print(type(user))


# Access dictionary values using their keys.

print(user["name"])
print(user["age"])
print(user["role"])


# Add a new key-value pair:

user["city"] = "Lahore"

print(user)


# Update an existing value:

user["age"] = 79

print(user)


# ============================================================
# 9. NONE -> NoneType
# ============================================================
# None represents the absence of a value.
#
# It means that a variable currently has no value.
#
# None is different from:
# 0
# False
# ""
#
# None specifically represents "no value".


result = None

print(result)
print(type(result))


# Check if a variable contains None:

print(result is None)


# ============================================================
# QUICK REVISION
# ============================================================

# str
# -> Text
# -> Example: "Hello"

# int
# -> Whole numbers
# -> Example: 10

# float
# -> Decimal numbers
# -> Example: 10.5

# bool
# -> True or False
# -> Example: True

# list
# -> Ordered and mutable collection
# -> Example: [1, 2, 3]

# tuple
# -> Ordered and immutable collection
# -> Example: (1, 2, 3)

# set
# -> Collection of unique values
# -> Example: {1, 2, 3}

# dict
# -> Key-value pairs
# -> Example: {"name": "Ali", "age": 20}

# NoneType
# -> Represents no value
# -> Example: None


# ============================================================
# CHECKING DATA TYPES
# ============================================================
# The type() function tells us the data type of a value.


name = "Salaar"
age = 23
price = 99.99
is_student = True
items = [1, 2, 3]
coordinates = (10, 20)
unique_numbers = {1, 2, 3}
user = {"name": "Ali"}
result = None

print(type(name))
print(type(age))
print(type(price))
print(type(is_student))
print(type(items))
print(type(coordinates))
print(type(unique_numbers))
print(type(user))
print(type(result))