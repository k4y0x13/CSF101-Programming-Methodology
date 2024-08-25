# Exercise

# Python Control Structures

These exercises are designed to help you practice working with control structures in Python. Follow each step carefully and try to predict the output before running the code.

## File Organization

We'll add a new directory called `control_structures` to your existing file structure. The updated structure will look like this:

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
└── control_structures/
    ├── conditionals.py
    ├── loops.py
    └── break_continue.py
```

Create a new directory called `control_structures` inside your `csf101-python_exercises` directory.

## Exercise 1: Conditional Statements

File: `control_structures/conditionals.py`

Create a new file called `conditionals.py` in the `control_structures` directory and complete the following exercises in this file.

1. Write an if-else statement to check if a number is positive or negative.

   ```python
   number = 10
   if number > 0:
       print("The number is positive.")
   else:
       print("The number is non-positive.")
   ```

   Expected output: `The number is positive.`

2. Extend the previous example to include zero as a separate case.

   ```python
   number = 0
   if number > 0:
       print("The number is positive.")
   elif number < 0:
       print("The number is negative.")
   else:
       print("The number is zero.")
   ```

   Expected output: `The number is zero.`

3. Write a program that assigns a letter grade based on a numerical score.

   ```python
   score = 85
   if score >= 90:
       grade = "A"
   elif score >= 80:
       grade = "B"
   elif score >= 70:
       grade = "C"
   elif score >= 60:
       grade = "D"
   else:
       grade = "F"
   print(f"Your grade is: {grade}")
   ```

   Expected output: `Your grade is: B`

4. Use a ternary operator to check if a number is even or odd.

   ```python
   number = 7
   result = "even" if number % 2 == 0 else "odd"
   print(f"The number is {result}.")
   ```

   Expected output: `The number is odd.`

5. Implement a simple calculator using if-elif-else statements.

   ```python
   num1 = 10
   num2 = 5
   operator = "+"

   if operator == "+":
       result = num1 + num2
   elif operator == "-":
       result = num1 - num2
   elif operator == "*":
       result = num1 * num2
   elif operator == "/":
       result = num1 / num2 if num2 != 0 else "Error: Division by zero"
   else:
       result = "Error: Invalid operator"

   print(f"Result: {result}")
   ```

   Expected output: `Result: 15`

## Exercise 2: Loops

File: `control_structures/loops.py`

Create a new file called `loops.py` in the `control_structures` directory and complete the following exercises in this file.

6. Write a for loop to print numbers from 1 to 5.

   ```python
   for i in range(1, 6):
       print(i)
   ```

   Expected output:

   ```
   1
   2
   3
   4
   5
   ```

7. Use a while loop to print numbers from 5 to 1 in reverse order.

   ```python
   count = 5
   while count > 0:
       print(count)
       count -= 1
   ```

   Expected output:

   ```
   5
   4
   3
   2
   1
   ```

8. Write a for loop to calculate the sum of numbers from 1 to 10.

   ```python
   total = 0
   for num in range(1, 11):
       total += num
   print(f"The sum of numbers from 1 to 10 is: {total}")
   ```

   Expected output: `The sum of numbers from 1 to 10 is: 55`

9. Use a for loop to iterate over a list and print each item.

   ```python
   fruits = ["apple", "banana", "cherry"]
   for fruit in fruits:
       print(fruit)
   ```

   Expected output:

   ```
   apple
   banana
   cherry
   ```

10. Write a nested loop to create a multiplication table for numbers 1 to 3.

    ```python
    for i in range(1, 4):
        for j in range(1, 4):
            print(f"{i} * {j} = {i*j}")
        print()  # Print a newline after each inner loop
    ```

    Expected output:

    ```
    1 * 1 = 1
    1 * 2 = 2
    1 * 3 = 3

    2 * 1 = 2
    2 * 2 = 4
    2 * 3 = 6

    3 * 1 = 3
    3 * 2 = 6
    3 * 3 = 9
    ```

## Exercise 3: Break and Continue Statements

File: `control_structures/break_continue.py`

Create a new file called `break_continue.py` in the `control_structures` directory and complete the following exercises in this file.

11. Use a break statement to exit a while loop when a certain condition is met.

    ```python
    count = 0
    while True:
        print(count)
        count += 1
        if count >= 5:
            break
    print("Loop ended")
    ```

    Expected output:

    ```
    0
    1
    2
    3
    4
    Loop ended
    ```

12. Use a continue statement to skip even numbers in a for loop.

    ```python
    for num in range(1, 6):
        if num % 2 == 0:
            continue
        print(num)
    ```

    Expected output:

    ```
    1
    3
    5
    ```

13. Write a loop that searches for a specific number in a list and stops when it's found.

    ```python
    numbers = [4, 2, 7, 1, 8, 3, 6]
    search_for = 8

    for num in numbers:
        if num == search_for:
            print(f"Found {search_for}!")
            break
        print(f"Not {search_for}...")
    ```

    Expected output:

    ```
    Not 8...
    Not 8...
    Not 8...
    Not 8...
    Found 8!
    ```

14. Implement a simple number guessing game using a while loop and break statement.

    ```python
    import random

    secret_number = random.randint(1, 10)
    attempts = 0

    while True:
        guess = int(input("Guess the number (1-10): "))
        attempts += 1

        if guess == secret_number:
            print(f"Congratulations! You guessed it in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")
    ```

    Sample run:

    ```
    Guess the number (1-10): 5
    Too low. Try again.
    Guess the number (1-10): 8
    Too high. Try again.
    Guess the number (1-10): 7
    Congratulations! You guessed it in 3 attempts.
    ```

15. Use a for loop with else to check if a number is prime.

    ```python
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    number = 17
    if is_prime(number):
        print(f"{number} is prime.")
    else:
        print(f"{number} is not prime.")
    ```

    Expected output: `17 is prime.`

Congratulations!

**Remember** to run each file separately to see the output of your exercises. You can do this by navigating to the appropriate directory in your terminal and running `python filename.py` (e.g., `python conditionals.py`).
