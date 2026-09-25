# A set is a collection of values where:
# Every value is unique
# Duplicate values are automatically removed
# Sets are unordered
# Sets are mutable, you can add or remove items


numbers = {1,2,3,4,5,6,7}
print(numbers)

fruits = {"apple", "banana", "orange", "apple"}
print(fruits)

my_set = {}
print(my_set)
print(type(my_set))


# Sets automatically remove duplicates 

names = {"Ali", "Ahmed", "Ali", "Sara", "Ahmed"}

print(names)

# Sets are unordered
# Don't expect a set to maintain a specific order

fruits = {"cherry", "banana", "Graphes"}
print(fruits)

 # print(fruits[0])  that's why this is not correct

# lists are ordered and sets are unordered

names = {"snobar", "ahmed", "sarfaraz", "zeeshan"}
names.add("hassan")

print(names)


# Adding multiple items by using update()

fruits = {"apple", "bananana"}
fruits.update(["graphes", "cherry", "mango"])
print(fruits)

# removing an item

fruits = {"apple", "banana", "orange"}
fruits.remove("banana")
print("fruits are = ", fruits)


# Removing items safely by using discard()

fruits = {"apple", "banana", "orange"}
fruits.discard("mango")

# Remove a Random Item by using pop()

fruits = {"apple", "banana", "orange"}

item = fruits.pop()

print(item)

# Remove Everything by using clear()

numbers = {1,2,3,4,5,6,7,8,9,90}
numbers.clear()

print(numbers)

# Check if Something Exists by usng in

numbers = {1,2,3,4,5,6,7,8,9,90}
print(1 in numbers)  # output will be true


# Set Length len()
numbers = {1,2,3,4,5,6,7,8,9,90}
print(len(numbers))