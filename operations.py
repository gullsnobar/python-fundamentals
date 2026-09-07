# ============================================================
# PYTHON OPERATORS
# ============================================================
# An operator is a symbol or keyword used to perform
# an operation on values or variables.
#
# Example:
# a + b
#
# Here:
# a and b = operands
# +       = operator
# ============================================================


# ============================================================
# 1. ARITHMETIC OPERATORS
# ============================================================
# Arithmetic operators are used to perform mathematical
# calculations such as addition, subtraction, multiplication,
# and division.
#
# Operators:
# +   Addition
# -   Subtraction
# *   Multiplication
# /   Division
# //  Floor Division
# %   Modulus (remainder)
# **  Exponent (power)


a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)


# ============================================================
# 2. ASSIGNMENT OPERATORS
# ============================================================
# Assignment operators are used to assign a value to
# a variable or update the value of an existing variable.
#
# =    Assign
# +=   Add and assign
# -=   Subtract and assign
# *=   Multiply and assign
# /=   Divide and assign
# //=  Floor divide and assign
# %=   Modulus and assign
# **=  Power and assign


score = 10

score += 5
print("After +=:", score)

score -= 2
print("After -=:", score)

score *= 2
print("After *=:", score)

score /= 2
print("After /=:", score)


# ============================================================
# 3. COMPARISON OPERATORS
# ============================================================
# Comparison operators are used to compare two values.
# They always return a Boolean value: True or False.
#
# ==   Equal to
# !=   Not equal to
# >    Greater than
# <    Less than
# >=   Greater than or equal to
# <=   Less than or equal to


age = 23

print("Equal:", age == 23)
print("Not Equal:", age != 20)
print("Greater Than:", age > 18)
print("Less Than:", age < 30)
print("Greater Than or Equal:", age >= 23)
print("Less Than or Equal:", age <= 20)


# IMPORTANT:
# =  is used for assignment
# == is used for comparison

name = "Salaar"

print(name == "Salaar")


# ============================================================
# 4. LOGICAL OPERATORS
# ============================================================
# Logical operators are used to combine multiple conditions.
#
# and  = True if both conditions are True
# or   = True if at least one condition is True
# not  = Reverses the Boolean value


age = 23
has_id = True

# AND
# Both conditions must be True.

print("AND:", age >= 18 and has_id)


# OR
# At least one condition must be True.

print("OR:", age >= 18 or has_id)


# NOT
# Reverses True to False and False to True.

print("NOT:", not has_id)


# ============================================================
# 5. MEMBERSHIP OPERATORS
# ============================================================
# Membership operators are used to check whether a value
# exists inside a sequence such as a string or list.
#
# in      = Checks if a value exists
# not in  = Checks if a value does not exist


name = "Python"

print("P in name:", "P" in name)
print("x in name:", "x" in name)
print("x not in name:", "x" not in name)


# Membership operators can also be used with lists.

languages = ["Python", "Java", "JavaScript"]

print("Python in languages:", "Python" in languages)
print("C++ not in languages:", "C++" not in languages)


# ============================================================
# 6. IDENTITY OPERATORS
# ============================================================
# Identity operators are used to check whether two variables
# refer to the same object in memory.
#
# is      = Checks if two variables are the same object
# is not  = Checks if two variables are not the same object


value = None

print("value is None:", value is None)
print("value is not None:", value is not None)


# IMPORTANT:
# == checks whether two values are equal.
# is checks whether two variables refer to the same object.


# ============================================================
# 7. BITWISE OPERATORS
# ============================================================
# Bitwise operators work with numbers at the binary/bit level.
#
# &   Bitwise AND
# |   Bitwise OR
# ^   Bitwise XOR
# ~   Bitwise NOT
# <<  Left Shift
# >>  Right Shift


x = 5
y = 3

print("Bitwise AND:", x & y)
print("Bitwise OR:", x | y)
print("Bitwise XOR:", x ^ y)
print("Bitwise NOT:", ~x)
print("Left Shift:", x << 1)
print("Right Shift:", x >> 1)


# ============================================================
# 8. OPERATOR PRECEDENCE
# ============================================================
# Operator precedence determines the order in which Python
# evaluates operators in an expression.
#
# Basic order:
#
# 1. ()
# 2. **
# 3. * / // %
# 4. + -
#
# Parentheses can be used to control the order of calculation.


result = 10 + 5 * 2

print("Result:", result)
# Multiplication happens first:
# 5 * 2 = 10
# 10 + 10 = 20


result = (10 + 5) * 2

print("Result with parentheses:", result)
# Parentheses happen first:
# 10 + 5 = 15
# 15 * 2 = 30