# Exercise

# Exercises: Variables and Data Types

These exercises are designed to help you practice working with variables and different data types in Python. Follow each step carefully and try to predict the output before running the code.

## File Organization

To keep your work organized, we'll use the following file structure:

```
csf101-python_exercises/
│
├── basics/
│   ├── numbers.py
│   ├── strings.py
│   └── booleans.py
│
└── data_structures/
    ├── lists.py
    └── dictionaries.py
```

Create a new directory called `python_exercises` and navigate into it. Then, create two subdirectories: `basics` and `data_structures`.

## Exercise 1: Working with Integers and Floats

File: `basics/numbers.py`

Create a new file called `numbers.py` in the `basics` directory and complete the following exercises in this file.

1. Create a variable `age` and assign it your age as an integer.

   ```python
   age = 25  # Replace with your actual age
   print(age)
   ```

   Expected output: `25`

2. Create a variable `height` and assign it your height in meters as a float.

   ```python
   height = 1.75  # Replace with your actual height
   print(height)
   ```

   Expected output: `1.75`

3. Calculate your age in days (assume 365 days per year) and store it in a variable `age_in_days`.

   ```python
   age_in_days = age * 365
   print(age_in_days)
   ```

   Expected output: `9125`

4. Divide your `age` by 7 and print the result.

   ```python
   result = age / 7
   print(result)
   ```

   Expected output: `3.5714285714285716`

   Note: The result is a float, even though we started with integers.

## Exercise 2: Working with Strings

File: `basics/strings.py`

Create a new file called `strings.py` in the `basics` directory and complete the following exercises in this file.

5. Create a variable `name` and assign it your full name as a string.

   ```python
   name = "John Doe"  # Replace with your actual name
   print(name)
   ```

   Expected output: `John Doe`

6. Use string concatenation to create a greeting message.

   ```python
   greeting = "Hello, " + name + "!"
   print(greeting)
   ```

   Expected output: `Hello, John Doe!`

7. Use f-strings to create the same greeting message.

   ```python
   greeting_f = f"Hello, {name}!"
   print(greeting_f)
   ```

   Expected output: `Hello, John Doe!`

8. Print the length of your name.

   ```python
   name_length = len(name)
   print(name_length)
   ```

   Expected output: `8`

   Warning: Remember that spaces count as characters too!

## Exercise 3: Working with Booleans

File: `basics/booleans.py`

Create a new file called `booleans.py` in the `basics` directory and complete the following exercises in this file.

9. Create two boolean variables, `is_student` and `is_employed`, and assign them appropriate values.

   ```python
   is_student = True
   is_employed = False
   print(is_student, is_employed)
   ```

   Expected output: `True False`

10. Use the `and` operator to check if you are both a student and employed.

    ```python
    is_student_and_employed = is_student and is_employed
    print(is_student_and_employed)
    ```

    Expected output: `False`

11. Use the `or` operator to check if you are either a student or employed.
    ```python
    is_student_or_employed = is_student or is_employed
    print(is_student_or_employed)
    ```
    Expected output: `True`

## Exercise 4: Type Conversion

File: `basics/type_conversion.py`

Create a new file called `type_conversion.py` in the `basics` directory and complete the following exercises in this file.

12. Convert your `age` to a string and concatenate it with a message.

    ```python
    age = 25  # Use the same age as in numbers.py
    age_str = str(age)
    message = "I am " + age_str + " years old."
    print(message)
    ```

    Expected output: `I am 25 years old.`

13. Try to convert a string to an integer.

    ```python
    num_str = "42"
    num_int = int(num_str)
    print(num_int)
    ```

    Expected output: `42`

14. Now try to convert a non-numeric string to an integer.

    ```python
    non_num_str = "Hello"
    try:
        non_num_int = int(non_num_str)
        print(non_num_int)
    except ValueError as e:
        print(f"Error: {e}")
    ```

    Expected output: `Error: invalid literal for int() with base 10: 'Hello'`

    Note: This will raise a ValueError, which we catch and print.

## Exercise 5: Working with Lists

File: `data_structures/lists.py`

Create a new file called `lists.py` in the `data_structures` directory and complete the following exercises in this file.

15. Create a list of your favorite fruits.

    ```python
    fruits = ["apple", "banana", "cherry"]
    print(fruits)
    ```

    Expected output: `['apple', 'banana', 'cherry']`

16. Add a new fruit to your list using the `append()` method.

    ```python
    fruits.append("date")
    print(fruits)
    ```

    Expected output: `['apple', 'banana', 'cherry', 'date']`

17. Access and print the second fruit in your list.

    ```python
    second_fruit = fruits[1]
    print(second_fruit)
    ```

    Expected output: `banana`

    Warning: Remember that list indices start at 0!

## Exercise 6: Working with Dictionaries

File: `data_structures/dictionaries.py`

Create a new file called `dictionaries.py` in the `data_structures` directory and complete the following exercises in this file.

18. Create a dictionary with information about yourself.

    ```python
    name = "John Doe"  # Use the same name as in strings.py
    age = 25  # Use the same age as in numbers.py
    height = 1.75  # Use the same height as in numbers.py
    is_student = True  # Use the same value as in booleans.py

    person_info = {
        "name": name,
        "age": age,
        "height": height,
        "is_student": is_student
    }
    print(person_info)
    ```

    Expected output: `{'name': 'John Doe', 'age': 25, 'height': 1.75, 'is_student': True}`

19. Add your favorite color to the dictionary.

    ```python
    person_info["favorite_color"] = "blue"  # Replace with your actual favorite color
    print(person_info)
    ```

    Expected output: `{'name': 'John Doe', 'age': 25, 'height': 1.75, 'is_student': True, 'favorite_color': 'blue'}`

20. Try to access a key that doesn't exist in the dictionary.

    ```python
    try:
        print(person_info["weight"])
    except KeyError as e:
        print(f"Error: {e}")
    ```

    Expected output: `Error: 'weight'`

    Note: This will raise a KeyError because 'weight' is not a key in our dictionary.

**Congratulations!**

## Final Notes on File Organization

- Keeping related concepts in the same directory (`basics` or `data_structures`) helps in organizing your learning process.
- As you progress in your Python journey, you can add more directories for advanced topics (e.g., `functions`, `classes`, `modules`).
- Always try to keep your code organized - it's a good habit that will help you as you work on larger projects.

Remember to run each file separately to see the output of your exercises. You can do this by navigating to the appropriate directory in your terminal and running `python filename.py` (e.g., `python numbers.py`).
