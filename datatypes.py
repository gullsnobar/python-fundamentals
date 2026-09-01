# Python Data Types

## What is a Data Type?

A data type tells Python what kind of data a variable contains.

```python
name = "Salaar"
age = 23
is_student = True
```

Check the type using `type()`:

```python
print(type(name))
print(type(age))
print(type(is_student))
```

### Access Characters

We can access characters of a string using indexes.

```python
print(name[0])  # S
print(name[2])  # l
```

Python indexing starts from `0`.

---

# Main Python Data Types

### 1. String → `str`

Used for text.

```python
brand_name = "Gucci"
student_name = "Ijaz"

print(brand_name)
print(student_name)
```

---

### 2. Integer → `int`

Used for whole numbers.

```python
age = 45

print(age)
print(type(age))
```

---

### 3. Float → `float`

Used for decimal numbers.

```python
number = 56.8

print(number)
```

---

### 4. Boolean → `bool`

Used for `True` or `False` values.

```python
is_logged_in = True
is_passed = False

print(is_passed)
```

---

### 5. List → `list`

Used to store multiple values in an **ordered collection**.

We use square brackets `[]`.

Lists are **mutable**, which means we can change their values.

```python
items = [3, 9, 93, 4, 5, 67, 23]

print(items)
```

Example:

```python
items[0] = 100

print(items)
```

---

### 6. Tuple → `tuple`

Used for a **fixed collection** of values.

We use parentheses `()`.

Tuples are **immutable**, which means we cannot change their values.

```python
example = (1, 2, 3, 4, 5)

print(example)
```

---

### 7. Set → `set`

Used to store **unique values**.

Duplicates are automatically removed.

We use curly brackets `{}`.

```python
set_example = {67, 9, 5, 9, 2.3, 6, 1, 6}

print(set_example)
```

---

### 8. Dictionary → `dict`

Used to store data in **key-value pairs**.

Dictionaries are very important for **backend development and APIs**.

```python
user = {
    "name": "Amjad",
    "age": 78,
    "role": "Software Engineer"
}

print(user)
```

Access values using keys:

```python
print(user["name"])
print(user["age"])
```

---

### 9. NoneType → `None`

`None` means there is currently **no value**.

```python
result = None

print(result)
print(type(result))
```

Output:

```text
None
<class 'NoneType'>
```
