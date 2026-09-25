# Python Loops
# There are mainly two loops you need to know well.

# for loop, while loop

# for loop
# You use a for loop when you want to process each item in a collection.

users = ["Ali", "Ahmed", "Sara"]
for user in users:
    print(user)


# loop through a list

products = ["Laptop", "Phone", "Mouse"]
for product in products:
    print(f"Processing {product}")

orders = [101, 102, 103, 103, 104, 108]

for order_id in orders:
    print(f"Processing order {order_id}")


# range()
# range() is useful when you need to repeat something a specific number of items.

for i in range(6):
    print(i)

for j in range(10):
    print(j)


# enumerate()
# This is very useful

users = ["ali", "ahmed", "kamran"]

# If you want both index and value you could do this.

for index, user in enumerate(users):
   print(index, user)

# Real-world example

products = ["Laptop", "Phone", "Keyboard"]
for number, product in enumerate(products, start=1):
    print(f"{number}. {product}")


# Loop through dictionaries

user = {
    "name": "Ibrahim",
    "age": 23,
    "city": "Lahore"
}

for key in user:
    print(key)

#  Dictionary Values

for value in user.values():
    print(value)


settings = {
    "theme": "dark",
    "language": "English",
    "notification": True
}

for setting, value in settings.items():
    print(f"{setting}:{value}")


# break means stop the loop completely

users = ["Ali", "Ahmed", "Sara", "John"]

for user in users:
    if user == "Sara":
        break

    print(user)    

# Continue means skip the current iteration and move to the next one.

numbers = [1, 2, 3, 4, 5]

for number in numbers:
    if number == 3:
        continue

    print(number)


# while loop
# Use while when you want to continue running while a conditions remains true.

count = 1

while count <= 5:
    print(count)
    count += 1


# Real world while loop

attempt = 1

while attempt <= 3:
    print(f"Attempt {attempt}")

    attempt += 1


# while + break

while True:
    user_input = input("Enter 'exit' to stop: ")

    if user_input == "exit":
        break


# enumerate() is used when you are looping over a collection and you need both the item's value and its position/index at the same time.        