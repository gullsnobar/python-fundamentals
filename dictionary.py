# What is Deictionary?

# A dictionary stores values in key ---> value pairs

# key       value
# ----------------
# name      Gull
# age       25
# city      Lahore


user = {
    "name": "Gull Snobar",
    "age": 33,
    "city": "lahore"
}

print(user)

# Accessing values

person = {
    "name": "Ahmed",
    "age": 54,
    "job": "Developer"
}
print(person["name"])
print(person["age"])

# What Happens If the Key Doesn't Exist?

person = {
    "name": "Kousar",
    "age" : 43
}
# print(person["city"])  this is keyError

# This is why .get() is very useful

person = {
    "name": "Ali Ansari",
    "age": 34
}
print(person.get("name"))


# Adding a new key

person = {
    "name": "Muneeb",
    "age": 24
}
person["city"] = "Lahore"
print(person)

# updateing an existhing value

person = {
    "name": "Ali",
    "age": 25
}

person["age"] = 26

print(person)

# update() --> You can update multiple values at once.

person = {
    "name": "Snobar",
    "age" : 22
}

person.update({
    "age" : 24,
    "city": "Lahore"
})

print(person)



# Removing a key by using pop()

person = {
    "name": "Ali",
    "age" : 23,
    "city": "kasur"
}

person.pop("age")
print("Person info is here = ", person)


# You can also delete a key using del

person = {
    "name" : "Ali",
    "age" : 25
}
del person["age"]
print(person)