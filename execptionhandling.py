# 1.  Python Exception Handling
# An exception is an error/event that occurs while your Python program is running and interrupts the normal flow of execution.


# 2. Why Do We Need Exception Handling?
# Imagine you're building an application that asks the user for a number:

age = int(input("Enter your age: "))

# but if user enters 24 everything is fine but what if they enter hello python will raise ValueError

# Without handling the exception, your program crashes.

# Exception handling allows you to say:

# If this specific problem happens, handle it properly instead of crashing the application.

try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Please enter a valid number.")    

# Common Python Exceptions You Should Know

# 1. ValueError
# This value has the wrong format

age = int("hello")
# raises ValueError


# 2. TypeError
# You are using an incompatible type.

result = "10" + 4  # also raises typeError


# 3. ZeroDivisionError

result = 10 / 0  # raises ZeroDivisionError

# 4. KeyError
# Trying to access a dictionary key that does not exist.

user = {
    "name": "Gull"
}

print(user["email"])


# 5. IndexError
# Tring to access a list index that does not exist.

users = ["Gull", "Rehman", "Shafaq"]
print(users[6])  # raises indexerror



# 6. FileNotFoundError

# Trying to open a file that doesn't exist.

file = open("users.txt")

# If the file doesn't exist:

# FileNotFoundError

# 7. PermissionError
# The program does not have permission to access something.

# 8. ConnectionError

# A network connection fails.

# You'll encounter this when working with APIs, databases, external services, etc.


# You can also use else
# else runs only if the try block succeeds

try:
    number = input(input("Enter a number: "))
except ValueError:
    print("Invalid number. ")  
else:
    print(f"You entered {number}")      


# finally

# finally is used when something must happen regardless of whether an exception occured.

try:
    file = open("users.txt")

    data = file.read()

except FileNotFoundError:
    print("File not found.")

finally:
    print("Operation finished.")