# Practical 3b: Practicing Python Loops and Logical Conditions

## Objective
In this lab, you will implement both recursive and iterative approaches to generate Fibonacci sequences in Python. This exercise will help you understand the differences between recursive and iterative problem-solving techniques, as well as analyze their performance characteristics.

## Prerequisites
- Basic knowledge of Python syntax
- Understanding of functions in Python
- Familiarity with recursion and iteration concepts

## Lab Steps
## Step 1: Python Operators
### Looking into python operators with print statements
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
```

## Step 2: If-Else Statements
### Trying out if, elif and else
```python
a = 33
b = 200
if b > a:
    print("b is greater than a")
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")
```

## Step 3: Match case Statements
### Printing different days
```python
def main():
    day = 8
    match day:
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("Wednesday")
        case 4:
            print("Thursday")
        case 5:
            print("Friday")
        case 6:
            print("Saturday")
        case 7:
            print("Sunday")
        case _:
            print("Not a weekday")
main()
```

## Step 4: While Loops
### While Loop
A guessing game using a while loop
```python
import random
a = 10
b = random.randint(0,20)
while(c != b):
    c = int(input("Enter Guess! "))
    if (c == b):
        print("You won!")
        break
    else:
        print("Wrong Answer, Try Again!")
```


Remember to analyze the time and space complexity of each approach and consider how they might perform with very large inputs. 
