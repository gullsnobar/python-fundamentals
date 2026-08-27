
# variables
# A variable is a name that refers to a value/object stored in memory.

name = "Gull"
age = 25
salary = 50000
is_student = True


print(name)
print(age)

# Python is dynamically typed. It automatically determine the types.

print(type(salary))
print(type(is_student))

# Variables can change their value

age = 22
print(age)

age = 23
print(age)


# You should give variables meaningful names.

student_name = "Gulll"
student_age = 22
total_marks = 457

# Examples

price = 4000
quantity = 5

total_price = price * quantity
print(total_price)

# Rules for naming variables
# Python has some rules.

# Rule 1 — Start with a letter or underscore

name = "Tayyab"
_age = 23

# Rule 2 — Numbers can be used after the first character

student1 = "Mihra"
student2 = "Snobar"

# Rule 3 — Don't use spaces
# student name = "Gull" --> this is invalid

student_name = "Amjad"

# Rule 4 — Python is case-sensitive

name = "Gull"
Name = "Sania";
NAME = "Ahmed"
print(NAME)

# you can Assign the same value to multiple variables

x = y = z = 100
print(x)
print(y)
print(z)

# Swaping Variables

a = 10
b = 20

a, b = b, a
print(a)

# Practical Examples

student_name = "Snobar";
student_age = 22
student_marks = 998;
is_passed = True

print("Student Name:", student_name)
print("Student Age:", student_age)
print("Marks:", student_marks)
print("Passed", is_passed)

# variables + User Input

name = input("Enter you name: ")
print("Hello", name)

age = input("Enter you age: ")
print("your age is: ", age)


# Calculator
# Let's combine variables, input, and operators.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

sum_result = num1 + num2
print("Sum: ", sum_result)