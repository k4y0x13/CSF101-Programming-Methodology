# Practical 1: Python Basics

## Python Comments
This is done with the # character at the beginning of the line
```python
# This is a comment line in the code
```

## Creating a Function
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

## Basic Data Types - Integer, Float, Boolean, None and Type Casting
```python
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
## Basic Data Types: String and Manipulations
``` Python
print("Hello!!!!")
print("This is my first script!")
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# String functions
print(len(a))
print(a.upper())
print(a.lower())
print(a.count('i'))
print(a.find('d'))
print(a.split())

# String Concatenation
b = "Hello"
c = "Hello"
d = b + "!!" + c + "??"
print(d)

# String replication
print("Alice" * 5)

# String formatting
name = "Karma"
print(f"Hello {name}")
print("Greeting to you, {}".format(name))
Number = 2
print("There are %d %s in the class" %(Number, name))
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

## Class excercise:
**Q1. Array manipulation:**  
Refer to the following documentation on python list methods [Link](https://www.w3schools.com/python/python_ref_list.asp)  
Create a python list and name it first_list as shown below:  
```python 
first_list = [0,1,2,3,4,5,6,7,8,9]
```  
Create a second empty list named inverse_list:  
```python
inverse_list = []
```  
Using the 
```python
 .append() 
 .pop()
 ```
 methods, create the implementation of a stack whereby you de-que elements from the first list
and enqueee them into the second list. Your output must be as follows:
```python
 inverse_list = [9,8,7,6,5,4,3,2,1,0]
 ```

Sample scaffold (fill up with logic and code where necesarry):
```python
first_list = [0,1,2,3,4,5,6,7,8,9]
inverse_list = [9,8,7,6,5,4,3,2,1,0]

index = 9
#Hint, use a while loop to loop throught first list from the last index
while index < :
  inverse_list.append()
  index = 

print(inverse_list)
 ```

**Q2. Implementing Functions**  
Take your array invers implementation from question 1 and define a function known as reverse_array. Pass the 
first_list() as an argument into the array and ensure that inverse_list is returned when the function is called. 

```python

def reverse_array(first_list):
  #logic and code from Q1


reverse_array(first_list)
```  



