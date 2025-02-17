# Practical Work I
```python
import random
print("Hello!!!!")
print("This is my first script!")

pi = 3.14
pi2 = int(pi)
print(pi)
print(pi2)

pi3 = "3.14"
print(type(pi3))
pi4 = float(pi3)
print(type(pi4))

print(0<1)
print(1>0)
bool(0)
bool(1)
bool("Hello")

x = None
print(x)

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
while(c != b):
    c = int(input("Enter Guess!\n"))
    if (c == b):
        print("You won!")
        break
```
