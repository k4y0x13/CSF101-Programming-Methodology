# Practical Work I
import random
a = 10
b = random.randint(0,20)
c = 100
print("Hello!!!!")
print("This is my first script!")

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

pi = 3.14
pi2 = int(pi)
print(pi)
print(pi2)

pi3 = "3.14"
print(type(pi3)
pi4 = float(pi3)
print(type(pi4)
