# Tuples in Python
# A tuple is an ordered collection of values, similar to the lists.

skills = ("python", "javascript", "C++")
print(skills);

# skills[0] = "python"  this would not work because tuples are immuteable
# print(skills)

names = ("snobar", "shafaq", "nouman")
print(names)

# The main difference between lists and tuples is that lists can be changed but tuples can not be changed after creation.


# If Lists can store multiple values, why do I need Tuples?
# Use a tuple when a condition of values should not be changed.

numbers = (10,20,30,40,50,60,70)
print(numbers)



# Tuple Without Parentheses
# Parentheses are not actually what make something a tuple.


user = "Ali", 24, "Pakistan"
print(user)

# Empty Tuple
# You can create an empty tuple

data = ()
print(type(data))

users = ("Snobar", "Maria", "Eman")
print(users[1])
print(users[-1])

# Tuple Slicing
# Tuple also supports slicing

numbers = (10,20,30,40,50,60,70)
print(numbers[1:4])

# The most imp difference between tuple ans lists is Mutability.

# List
# ↓
# Can change
# Can add
# Can remove

# Tuple
# ↓
# Cannot change
# Cannot add
# Cannot remove


# length in Tuples
numbers = (10,20,30,40,50,60,70)
print(len(numbers))


# in with Tuples

roles = ("editor", "admin" , "viewer")
if "admin" in roles:
    print("Admin is exists")


numbers = (10,20,30,40,50,60,70)
if 20 in numbers:
    print("20 is exists")

# Tuples intentionally have very few methods because they cannot be modified.

# The two important ones are:

# count()
# index()

# counts how many times a value appears.

numbers = (10,20,30,40,50,60,70)
print(numbers.count(10))

# index finds the position of a value.

users = ("Ali", "Ahmed", "Sara")
print(users.index("Ali"))

numbers = (10,20,30,40,50,60,70)
print(numbers.index(10))