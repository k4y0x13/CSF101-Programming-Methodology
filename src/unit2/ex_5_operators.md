# Exercise

# Python Operators

These exercises are designed to help you practice working with various operators in Python. Follow each step carefully and try to predict the output before running the code.

## File Organization

We'll add a new directory called `operators` to your existing file structure. The updated structure will look like this:

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
└── operators/
    ├── arithmetic.py
    ├── assignment.py
    ├── comparison.py
    ├── logical.py
    └── bitwise.py
```

Create a new directory called `operators` inside your `csf101-python_exercises` directory.

## Exercise 1: Arithmetic Operators

File: `operators/arithmetic.py`

Create a new file called `arithmetic.py` in the `operators` directory and complete the following exercises in this file.

1. Create two variables `a` and `b` with values 15 and 4 respectively.

   ```python
   a, b = 15, 4
   print(f"a = {a}, b = {b}")
   ```

   Expected output: `a = 15, b = 4`

2. Perform addition, subtraction, multiplication, and division with these variables.

   ```python
   print(f"Addition: {a + b}")
   print(f"Subtraction: {a - b}")
   print(f"Multiplication: {a * b}")
   print(f"Division: {a / b}")
   ```

   Expected output:

   ```
   Addition: 19
   Subtraction: 11
   Multiplication: 60
   Division: 3.75
   ```

3. Use the modulus operator to find the remainder when `a` is divided by `b`.

   ```python
   print(f"Modulus: {a % b}")
   ```

   Expected output: `Modulus: 3`

4. Use the exponentiation operator to calculate `a` to the power of `b`.

   ```python
   print(f"Exponentiation: {a ** b}")
   ```

   Expected output: `Exponentiation: 50625`

5. Use floor division to divide `a` by `b`.
   ```python
   print(f"Floor Division: {a // b}")
   ```
   Expected output: `Floor Division: 3`

## Exercise 2: Assignment Operators

File: `operators/assignment.py`

Create a new file called `assignment.py` in the `operators` directory and complete the following exercises in this file.

6. Create a variable `x` with an initial value of 10.

   ```python
   x = 10
   print(f"Initial x: {x}")
   ```

   Expected output: `Initial x: 10`

7. Use the `+=` operator to add 5 to `x`.

   ```python
   x += 5
   print(f"After x += 5: {x}")
   ```

   Expected output: `After x += 5: 15`

8. Use the `-=` operator to subtract 3 from `x`.

   ```python
   x -= 3
   print(f"After x -= 3: {x}")
   ```

   Expected output: `After x -= 3: 12`

9. Use the `*=` operator to multiply `x` by 2.

   ```python
   x *= 2
   print(f"After x *= 2: {x}")
   ```

   Expected output: `After x *= 2: 24`

10. Use the `/=` operator to divide `x` by 4.
    ```python
    x /= 4
    print(f"After x /= 4: {x}")
    ```
    Expected output: `After x /= 4: 6.0`

## Exercise 3: Comparison Operators

File: `operators/comparison.py`

Create a new file called `comparison.py` in the `operators` directory and complete the following exercises in this file.

11. Create two variables `a` and `b` with values 10 and 5 respectively.

    ```python
    a, b = 10, 5
    print(f"a = {a}, b = {b}")
    ```

    Expected output: `a = 10, b = 5`

12. Use comparison operators to compare `a` and `b`.

    ```python
    print(f"a == b: {a == b}")
    print(f"a != b: {a != b}")
    print(f"a > b: {a > b}")
    print(f"a < b: {a < b}")
    print(f"a >= b: {a >= b}")
    print(f"a <= b: {a <= b}")
    ```

    Expected output:

    ```
    a == b: False
    a != b: True
    a > b: True
    a < b: False
    a >= b: True
    a <= b: False
    ```

13. Create a variable `c` with value 10 and compare it with `a`.
    ```python
    c = 10
    print(f"a == c: {a == c}")
    ```
    Expected output: `a == c: True`

## Exercise 4: Logical Operators

File: `operators/logical.py`

Create a new file called `logical.py` in the `operators` directory and complete the following exercises in this file.

14. Create two boolean variables `x` and `y`.

    ```python
    x = True
    y = False
    print(f"x = {x}, y = {y}")
    ```

    Expected output: `x = True, y = False`

15. Use the `and` operator with `x` and `y`.

    ```python
    print(f"x and y: {x and y}")
    ```

    Expected output: `x and y: False`

16. Use the `or` operator with `x` and `y`.

    ```python
    print(f"x or y: {x or y}")
    ```

    Expected output: `x or y: True`

17. Use the `not` operator with `x` and `y`.
    ```python
    print(f"not x: {not x}")
    print(f"not y: {not y}")
    ```
    Expected output:
    ```
    not x: False
    not y: True
    ```

## Exercise 5: Bitwise Operators

File: `operators/bitwise.py`

Create a new file called `bitwise.py` in the `operators` directory and complete the following exercises in this file.

18. Create two variables `a` and `b` with values 5 (101 in binary) and 3 (011 in binary) respectively.

    ```python
    a, b = 5, 3
    print(f"a = {a} (binary: {bin(a)}), b = {b} (binary: {bin(b)})")
    ```

    Expected output: `a = 5 (binary: 0b101), b = 3 (binary: 0b11)`

19. Use the bitwise AND operator on `a` and `b`.

    ```python
    print(f"a & b: {a & b} (binary: {bin(a & b)})")
    ```

    Expected output: `a & b: 1 (binary: 0b1)`

20. Use the bitwise OR operator on `a` and `b`.
    ```python
    print(f"a | b: {a | b} (binary: {bin(a | b)})")
    ```
    Expected output: `a | b: 7 (binary: 0b111)`

Congratulations!

Remember to run each file separately to see the output of your exercises. You can do this by navigating to the appropriate directory in your terminal and running `python filename.py` (e.g., `python arithmetic.py`).
