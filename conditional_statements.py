# Conditional statements in Python
# A conditional statement allows your program to make a decision based on a condition.


age = 20

if age >= 18:
    print("You are an adult.")
       

# Indentation is VERY Important in Python

# This is different from languages like JavaScript.

# Python uses indentation to determine which code belongs to the if.


# if + else

age = 16

if age >= 18:
    print("You can enter the club.")
else:
    print("You cannot enter the club.")


# elif
# What if there are multiple possibilities? We can use elif to check for multiple conditions.

marks = 75

if marks >= 90:
    print("You got an A grade.")
elif marks >= 80:
    print("You got a B grade.")    
elif marks >= 70:
    print("You got a C grade.")    
else:
    print("You failed the exam.")



# Real World login example

email = "gull09@gmail.com"
password = "paswword@123"

if email ==  "gull09@gmail.com" and password == "paswword@123":
    print("Login successful.")
else:
    print("Invalid email or password.")

# Real-World Example: Subscription Plan

plan = "premium"

if plan == "free":
    print("You have access to basic features.")
elif plan == "premium":
    print("You have access to premium features.")
elif plan == "enterprise":
    print("You have access to enterprise features.")
else:
    print("Invalid subscription plan.")        

# and operator means both conditions must be true.

age = 24

has_ticket = True

if age >= 18 and has_ticket:
    print("You can enter the concert.")

# or means at least one condition must be true.

is_admin = False
is_manager = True

if is_admin or is_manager:
    print("You have access to the dashboard.")

# not reverses a Boolean value.

is_logged_in = False

if not is_logged_in:
    print("Please login")

