
# Python Basics Cheatsheet

## 1. Variables & Data Types
```python
# Integer, Float, String, Boolean
x = 10            # int
y = 3.14          # float
name = "Rupa"     # str
is_active = True  # bool
```

## 2. Basic Data Structures
```python
# List
my_list = [1, 2, 3]
my_list.append(4)  # Add element

# Tuple (Immutable)
my_tuple = (1, 2, 3)

# Dictionary
my_dict = {"name": "Rupa", "age": 25}
print(my_dict["name"])  # Access value

# Set (Unique items)
my_set = {1, 2, 3}
my_set.add(4)
```

## 3. Conditional Statements
```python
x = 10
if x > 5:
    print("Greater")
elif x == 5:
    print("Equal")
else:
    print("Smaller")
```

## 4. Loops
```python
# For Loop
for i in range(5):
    print(i)

# While Loop
x = 0
while x < 5:
    print(x)
    x += 1
```

## 5. Functions
```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Rupa"))  # Output: Hello, Rupa!
```

## 6. Classes & Objects
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"My name is {self.name}."

rupa = Person("Rupa", 25)
print(rupa.greet())
```

## 7. File Operations
```python
# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, Rupa!")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```

## 8. List Comprehensions
```python
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
```

## 9. Error Handling
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

## 10. Importing Modules
```python
import math
print(math.sqrt(16))  # 4.0
```

## 11. Useful Built-in Functions
```python
print(len("Rupa"))  # Length of a string
print(max([1, 2, 3]))  # Maximum
print(min([1, 2, 3]))  # Minimum
print(sum([1, 2, 3]))  # Sum
```
