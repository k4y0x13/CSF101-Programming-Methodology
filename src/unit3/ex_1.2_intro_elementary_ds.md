# Exercise

# Exercises: Data Structures in Python

These exercises are designed to help you practice working with various data structures in Python, focusing on arrays (lists) and their operations. Follow each step carefully and try to predict the output before running the code.

## File Organization

We'll use the following file structure for these exercises:

```
csf101-python_exercises/
└── data_structures/
    ├── arrays.py
    └── multi_dimensional_arrays.py
```

Create a new directory called `data_structures` inside your `csf101-python_exercises` directory if it doesn't already exist.

## Exercise 1: Working with Arrays (Lists)

File: `data_structures/arrays.py`

Create a new file called `arrays.py` in the `data_structures` directory and complete the following exercises in this file.

1. Create a list of your favorite colors.

   ```python
   colors = ["red", "blue", "green", "yellow"]
   print(colors)
   ```

   Expected output: `['red', 'blue', 'green', 'yellow']`

2. Access and print the second and last colors in your list.

   ```python
   print(colors[1])  # Second color
   print(colors[-1])  # Last color
   ```

   Expected output:

   ```
   blue
   yellow
   ```

   Warning: Remember that list indices start at 0! The second element has an index of 1.

3. Add a new color to your list using the `append()` method.

   ```python
   colors.append("purple")
   print(colors)
   ```

   Expected output: `['red', 'blue', 'green', 'yellow', 'purple']`

4. Remove the color "green" from your list using the `remove()` method.

   ```python
   colors.remove("green")
   print(colors)
   ```

   Expected output: `['red', 'blue', 'yellow', 'purple']`

   Warning: If the color doesn't exist in the list, you'll get a ValueError. Let's demonstrate this:

   ```python
   try:
       colors.remove("orange")
   except ValueError as e:
       print(f"Error: {e}")
   ```

   Expected output: `Error: list.remove(x): x not in list`

5. Create a static-like list with a fixed size of 5 elements, all initialized to None.

   ```python
   static_list = [None] * 5
   print(static_list)
   ```

   Expected output: `[None, None, None, None, None]`

6. Try to add an element beyond the fixed size of the static-like list.

   ```python
   try:
       static_list[5] = "New Element"
   except IndexError as e:
       print(f"Error: {e}")
   ```

   Expected output: `Error: list assignment index out of range`

   Note: This demonstrates the behavior of a static array, where you can't add elements beyond its initial size.

## Exercise 2: Array Operations

Continue in the `arrays.py` file.

7. Create a list of numbers and perform sorting operations.

   ```python
   numbers = [5, 2, 8, 1, 9, 3]
   print("Original list:", numbers)

   numbers.sort()
   print("Sorted list:", numbers)

   numbers.sort(reverse=True)
   print("Reverse sorted list:", numbers)
   ```

   Expected output:

   ```
   Original list: [5, 2, 8, 1, 9, 3]
   Sorted list: [1, 2, 3, 5, 8, 9]
   Reverse sorted list: [9, 8, 5, 3, 2, 1]
   ```

8. Find the index of a specific element in the list.

   ```python
   fruits = ["apple", "banana", "cherry", "date"]
   index = fruits.index("cherry")
   print(f"The index of 'cherry' is: {index}")
   ```

   Expected output: `The index of 'cherry' is: 2`

   Now, try to find an element that doesn't exist:

   ```python
   try:
       index = fruits.index("grape")
   except ValueError as e:
       print(f"Error: {e}")
   ```

   Expected output: `Error: 'grape' is not in list`

9. Use list slicing to create a new list from a subset of elements.

   ```python
   numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
   subset = numbers[2:7]
   print(subset)
   ```

   Expected output: `[2, 3, 4, 5, 6]`

   Warning: Remember that the end index in slicing is exclusive!

## Exercise 3: Multi-dimensional Arrays

File: `data_structures/multi_dimensional_arrays.py`

Create a new file called `multi_dimensional_arrays.py` in the `data_structures` directory and complete the following exercises in this file.

10. Create a 2D array (matrix) representing a tic-tac-toe board.

    ```python
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

    # Print the board
    for row in board:
        print(row)
    ```

    Expected output:

    ```
    [' ', ' ', ' ']
    [' ', ' ', ' ']
    [' ', ' ', ' ']
    ```

11. Make some moves on the tic-tac-toe board.

    ```python
    board[0][0] = "X"  # Top-left
    board[1][1] = "O"  # Center
    board[2][2] = "X"  # Bottom-right

    # Print the updated board
    for row in board:
        print(row)
    ```

    Expected output:

    ```
    ['X', ' ', ' ']
    [' ', 'O', ' ']
    [' ', ' ', 'X']
    ```

12. Try to access an element outside the board's dimensions.

    ```python
    try:
        print(board[3][0])
    except IndexError as e:
        print(f"Error: {e}")
    ```

    Expected output: `Error: list index out of range`

13. Create a 3D array representing a cube of numbers.

    ```python
    cube = [
        [[1, 2], [3, 4]],
        [[5, 6], [7, 8]],
        [[9, 10], [11, 12]]
    ]

    # Print the cube
    for layer in cube:
        for row in layer:
            print(row)
        print()  # Empty line between layers
    ```

    Expected output:

    ```
    [1, 2]
    [3, 4]

    [5, 6]
    [7, 8]

    [9, 10]
    [11, 12]
    ```

14. Access and modify an element in the 3D array.

    ```python
    print("Original value:", cube[1][0][1])
    cube[1][0][1] = 100
    print("Modified value:", cube[1][0][1])

    # Print the updated cube
    for layer in cube:
        for row in layer:
            print(row)
        print()  # Empty line between layers
    ```

    Expected output:

    ```
    Original value: 6
    Modified value: 100
    [1, 2]
    [3, 4]

    [5, 100]
    [7, 8]

    [9, 10]
    [11, 12]
    ```

## Final Notes

- These exercises cover the basics of working with arrays (lists) and multi-dimensional arrays in Python.
- Remember that Python lists are **dynamic**, allowing you to _add or remove elements easily_. This is _different from static arrays in some other programming languages_.
- When working with multi-dimensional arrays, _be careful with indexing to avoid IndexError exceptions._
- Practice these concepts by creating your own arrays and performing various operations on them.

To run these exercises, navigate to the `data_structures` directory in your terminal and run:

- `python arrays.py`
- `python multi_dimensional_arrays.py`

Make sure to experiment with the code and try your own variations to deepen your understanding of these concepts.
