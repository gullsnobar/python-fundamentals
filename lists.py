# 1. Python Lists
# What is a List?
#  A list is a collection which allows you to store multiple values inside one variable.

users = ["ali", "Noman", "Ahmed", "Ali", "Ijaz"]
print(users)

#  2. Why Lists Matter in Real Applications

#  In real applications, we constantly work with collections of data.

products = ["laptop", "mobile", "tablet", "desktop"]
print(products)

# 3. Creating Lists
# A list can contain different types of data.

# Strings
fruits = ["apple", "banana", "cherry", "kiwi"]
print(fruits)

# Integers
numbers = [1,2,3,4,5,6,7]
print(numbers)

# Floats
prices = [1.2, 2.8, 3.4, 2.7]
print(prices)

# Booleans
is_active = [True, False, True, False]
print(is_active)

# Mixed data types
data = ["apple", 1, 2.5, True]
print(data)

# Empty List
# You can create an empty list by using empty square brackets.

empty_list = []

# extremely common.

users = []

users.append("Snobar")
users.append("Sara")
print(users)


# 5. List Indexing
# Every item in a list has an index.

users = ["Ali", "Ahmed", "Sara"]

# The indexes are: 0, 1, 2

print(users[1]) # Output: Ahmed
print(users[2]) # Output: Sara


# 6. Negative Indexing

# Python also allows negative indexes.
# You can also use negative indexing to access the list items.


names = ["Ijaz", "Ali", "Kamran", "Sarah"]

print(names[-1]) # Output: Sarah
print(names[-2]) # Output: Kamran
print(names[-3]) # Output: Ali
print(names[-4]) # Output: Ijaz


# 7. Changing a List Item
# Lists are mutable.

Fruits = ["apple", "banana", "cherry", "kiwi"]
Fruits[1] = "graphes"

print(Fruits) 

# 8. len() — Get List Length

users = ["Ali", "Ahmed", "Sara"]
print(len(users))

fruits = ["apple", "banana", "cherry", "kiwi"]
print(len(fruits))


# 9. Adding Items with append()

numbers = [1,2,3,4,5]
numbers.append(6)
numbers.append(7)

print(numbers)


# 10. Adding Items with insert()

users = ["Fahad", "Kamran", "Ali", "Tariq"]
users.insert(0, "Gull_Snobar")
print(users)


# 11. remove()
# Remove an item based on its value.

students = ["Ali", "Ahmed", "Sara", "Kamran"]
students.remove("Sara")
print(students)


# 12. pop()
# Remove an item based on its index.

users = ["Ali", "Ahmed", "Sara", "Kamran"]
removed_user = users.pop(1)

print(removed_user) 
print(users)

# 13. delete()
# You can also delete an item based on its index using the del keyword.

fruits = ["apple", "banana", "cherry", "kiwi"]
del fruits[1]
del fruits[2]

print(fruits)



# Checking if an item exists in a list

numbers = [1, 2, 3, 4, 5]
if 3 in numbers:
    print("3 is present in the list.")

Fruits = ["apple", "banana", "cherry", "kiwi"]
if "oranges" not in Fruits:
    print("oranges is not present in the list.")


# List Slicing
# Slicing lets you get a portion of a list.

numbers = [10, 20, 30, 40, 50]
print(numbers[1:3])
print(numbers[2:4])



# Sorting Lists
numbers = [5, 2, 9, 1, 7]
numbers.sort()

print(numbers)

# Example: Sorting a list of strings

prices = [500, 100, 900, 300]

prices.sort()

print(prices)