# Python Functions
# A function is a reusable block of code that performs a specific task.

def greet(name):
    print(f"Hello {name}")

greet("Gull")    
greet("Ali")

# The main idea is write a logic at once and use it whenever you needed it.


# Parameters allow a function to receive data.
# In above function example name is paremeter and Gull is the argument.

# Parameter = variable defined in the function
# Argument = actual value passed to the function


# return ---> This is one of the most imp concept to understand


# Real world examples

def send_welcome_email():
    print("Sending welcome email.....")

send_welcome_email()


# Multiple Parameters
# You can pass multiple values

def calculate_total(price, quantity):
    return price * quantity

total = calculate_total(500, 3)
print(total)


# another example

def create_user(name, email, age):
    print(f"Name: {name}")
    print(f"Email:{email}")
    print(f"Age: {age}")

create_user(
    "Gull",
    "gullsnobar09@gmail.com",
    34
)

# return means Give this value back to whoever called me.
# This is why return is heavily used in real applications.

def add(a, b):
    return a + b

result = add(10,20)
print(result)


# A function can return different datatypes

# List

def get_users():
    return ["Gull", "Snobar", "kamran"]

users = get_users()
print(users)

# Dictionary

def get_user():
    return {
        "id": 1,
        "name": "Gulll",
        "email": "gullsnobar08@gmail.com"
    }

user = get_user()  
print(user["name"])  


# Lambda Functions
# You do not need to make every function a lambda

# A normal function

def square(number):
    return number * number

# A lambda function

square = lambda number: number * number
print(square(5))

# The most practical place you'll see lambda is with things like sorting.

users = [
    {"name": "Gull", "age": 2},
    {"name": "Ali", "age": 24},
    {"name": "Kamran", "age": 27}
]

users.sort(key=lambda user: user["age"])

print(users)