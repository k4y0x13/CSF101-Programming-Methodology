# Exercise

# Python Functions and Scope

These exercises are designed to help you practice working with functions and scope in Python. Follow each step carefully and try to predict the output before running the code.

## File Organization

We'll add a new directory called `functions_and_scope` to your existing file structure. The updated structure will look like this:

```
csf101-python_exercises/
│
├── basics/
│   ├── numbers.py
│   ├── strings.py
│   └── booleans.py
│
├── data_structures/
│   ├── lists.py
│   └── dictionaries.py
│
├── operators/
│   ├── arithmetic.py
│   ├── assignment.py
│   ├── comparison.py
│   ├── logical.py
│   └── bitwise.py
│
├── control_structures/
│   ├── conditionals.py
│   ├── loops.py
│   └── break_continue.py
│
└── functions_and_scope/
    ├── basic_functions.py
    ├── parameters_and_returns.py
    ├── scope.py
    └── recursion.py
```

Create a new directory called `functions_and_scope` inside your `csf101-python_exercises` directory.

## Exercise 1: Basic Functions

File: `functions_and_scope/basic_functions.py`

Create a new file called `basic_functions.py` in the `functions_and_scope` directory and complete the following exercises in this file.

1. Write a function called `greet` that prints "Hello, World!".

   ```python
   def greet():
       print("Hello, World!")

   greet()
   ```

   Expected output: `Hello, World!`

2. Modify the `greet` function to take a name parameter and greet that person.

   ```python
   def greet(name):
       print(f"Hello, {name}!")

   greet("Alice")
   ```

   Expected output: `Hello, Alice!`

3. Write a function called `square` that takes a number and returns its square.

   ```python
   def square(number):
       return number ** 2

   result = square(5)
   print(result)
   ```

   Expected output: `25`

4. Create a function called `is_even` that takes a number and returns True if it's even, False otherwise.

   ```python
   def is_even(number):
       return number % 2 == 0

   print(is_even(4))
   print(is_even(7))
   ```

   Expected output:

   ```
   True
   False
   ```

5. Write a function called `print_numbers` that prints numbers from 1 to n (inclusive).

   ```python
   def print_numbers(n):
       for i in range(1, n + 1):
           print(i)

   print_numbers(5)
   ```

   Expected output:

   ```
   1
   2
   3
   4
   5
   ```

## Exercise 2: Parameters and Return Values

File: `functions_and_scope/parameters_and_returns.py`

Create a new file called `parameters_and_returns.py` in the `functions_and_scope` directory and complete the following exercises in this file.

6. Write a function called `greet_with_default` that takes a name parameter with a default value of "Guest".

   ```python
   def greet_with_default(name="Guest"):
       print(f"Hello, {name}!")

   greet_with_default()
   greet_with_default("Bob")
   ```

   Expected output:

   ```
   Hello, Guest!
   Hello, Bob!
   ```

7. Create a function called `calculate_rectangle_area` that takes width and height as parameters and returns the area.

   ```python
   def calculate_rectangle_area(width, height):
       return width * height

   area = calculate_rectangle_area(5, 3)
   print(f"The area of the rectangle is: {area}")
   ```

   Expected output: `The area of the rectangle is: 15`

8. Write a function called `print_info` that takes any number of keyword arguments and prints them.

   ```python
   def print_info(**kwargs):
       for key, value in kwargs.items():
           print(f"{key}: {value}")

   print_info(name="Alice", age=30, city="New York")
   ```

   Expected output:

   ```
   name: Alice
   age: 30
   city: New York
   ```

9. Create a function called `min_max` that takes a list of numbers and returns both the minimum and maximum values.

   ```python
   def min_max(numbers):
       return min(numbers), max(numbers)

   result = min_max([5, 2, 8, 1, 9])
   print(f"Min: {result[0]}, Max: {result[1]}")
   ```

   Expected output: `Min: 1, Max: 9`

10. Write a function called `safe_divide` that takes two numbers and returns their division, or returns "Cannot divide by zero" if the second number is 0.

    ```python
    def safe_divide(a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b

    print(safe_divide(10, 2))
    print(safe_divide(5, 0))
    ```

    Expected output:

    ```
    5.0
    Cannot divide by zero
    ```

## Exercise 3: Scope

File: `functions_and_scope/scope.py`

Create a new file called `scope.py` in the `functions_and_scope` directory and complete the following exercises in this file.

11. Demonstrate the difference between local and global variables.

    ```python
    x = 10  # Global variable

    def print_x():
        x = 20  # Local variable
        print(f"Local x: {x}")

    print_x()
    print(f"Global x: {x}")
    ```

    Expected output:

    ```
    Local x: 20
    Global x: 10
    ```

12. Modify a global variable from within a function.

    ```python
    count = 0

    def increment():
        global count
        count += 1
        print(f"Count: {count}")

    increment()
    increment()
    print(f"Final count: {count}")
    ```

    Expected output:

    ```
    Count: 1
    Count: 2
    Final count: 2
    ```

13. Create a function that uses a nonlocal variable.

    ```python
    def outer():
        x = "outer"

        def inner():
            nonlocal x
            x = "inner"
            print(f"Inner x: {x}")

        inner()
        print(f"Outer x: {x}")

    outer()
    ```

    Expected output:

    ```
    Inner x: inner
    Outer x: inner
    ```

## Exercise 4: Recursion

File: `functions_and_scope/recursion.py`

Create a new file called `recursion.py` in the `functions_and_scope` directory and complete the following exercises in this file.

14. Write a recursive function to calculate the factorial of a number.

    ```python
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n - 1)

    print(factorial(5))
    ```

    Expected output: `120`

15. Create a recursive function to generate the nth Fibonacci number.

    ```python
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    print(fibonacci(7))
    ```

    Expected output: `13`

Congratulations!

Remember to run each file separately to see the output of your exercises. You can do this by navigating to the appropriate directory in your terminal and running `python filename.py` (e.g., `python basic_functions.py`).
