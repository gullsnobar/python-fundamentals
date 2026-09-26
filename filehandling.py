# Module
# A module is simply a Python file (.py) containing reusable code.

# Packages
# A package is basically a folder containing related Python modules.

# File Handling 
# Python allows you to:

# read, create, write, append and work with CSV/JSON


# Opening a File

file = open("data.txt", "r")

# The second argument is the mode, and r means read

# Reading a File

# You can read the entire file.

file = open("data.txt", "r")

content = file.read()

print(content)

file.close()


# Writing to a File

with open("data.txt", "w") as file:
    file.write("Hello World")

# Appending to a File
# If you want to add content without deleting existing content.

with open("data.txt", "a") as file:
    file.write("\nBob")


# pathlib ---> Imp
# pathlib is python's modern way of working with file and directory paths.

from pathlib import path

file_path = Path("data/users.txt")

print(file_path)

# JSON Files
# In real applications, you will frequently work with JSON.

{
    "name": "John",
    "age": 34
}

# Python provides the built-in json module.