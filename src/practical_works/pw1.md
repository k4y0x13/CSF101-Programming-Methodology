# Practical I: Python Basics

### Creating a Function
In Python a function is defined using the def keyword:
```python
def my_function():
  print("Hello from a function")
# Calling the function
my_function() 
```

## Scope
Notice how s has different defined value for the string in local scope within the function func() versus global scope for the overall python file.
```python
def func():
    # Local scope
    s = "Me too! (on local scope)"
    print(s)
# Global scope
s = "I love python! (on global scope)"
print(s)
```

## Basic Data Types
```python
print("Hello!!!!")
print("This is my first script!")

# Integer
pi = 3.14
pi2 = int(pi)
print(pi)
print(pi2)

# Float
pi3 = "3.14"
print(type(pi3))
pi4 = float(pi3)
print(type(pi4))

# Boolean
print(0<1)
print(1>0)
bool(0)
bool(1)
bool("Hello")

# None
x = None
print(x)
```
## Basic Data Structures
```python
# List
thislist = ["apple", "banana", "cherry"]
print(thislist)
print(len(thislist))
print(thislist.index("banana"))
thislist.remove("banana")
thislist.insert(1, "strawberry")
print(thislist)

# Tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)
print(len(thistuple))
print(type(thistuple))

# Set
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)
print(len(thisset))
print(type(myset))

# Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(thisdict["brand"])
```

## Python Operator, If-Else and While Loop
Looking into python operators with print statements and a guessing game
```python
import random
a = 10
b = random.randint(0,20)
c = 100
print("a is", a, "and", "b is", b)
print("The answer to a + b is", a + b)
print("a < b is", a < b)
print("a == b is", a == b)
print("a + b is", a + b)
print("a * b is", a * b)
print("a to the power of b is", a ** b)
# If-Else Statement in While Loop
while(c != b):
    c = int(input("Enter Guess! "))
    if (c == b):
        print("You won!")
        break
    else:
        print("Wrong Answer, Try Again!")
```
