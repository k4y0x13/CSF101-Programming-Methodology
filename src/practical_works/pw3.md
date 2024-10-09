# Practical Work III

# Practical 3: Fibonacci Sequence Generators

**Due Date:** 

**Submission:** GitHub repository link containing:
- Python source code (.py file)
- Lab report in markdown format
- Performance comparison results

## Learning Objectives
- Understand and implement recursive functions
- Implement iterative solutions
- Compare efficiency of recursive vs iterative approaches
- Practice algorithm analysis

## Requirements
Create a Python program that implements both recursive and iterative approaches to generate Fibonacci sequences with the following features:
1. Recursive Fibonacci generator
2. Iterative Fibonacci generator
3. Performance comparison between both approaches
5. Time complexity analysis

## Step-by-Step Implementation Guide

### Step 1: Recursive Implementation
1. Create a new Python file named `fibonacci_generators.py`
2. Implement the recursive Fibonacci function:
   ```python
   def fibonacci_recursive(n):
       if n <= 0:
           return 0
       elif n == 1:
           return 1
       else:
           return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
   ```

### Step 2: Iterative Implementation
1. Implement the iterative Fibonacci function:
   ```python
   def fibonacci_iterative(n):
       if n <= 0:
           return 0
       elif n == 1:
           return 1
           
       a, b = 0, 1
       for _ in range(2, n + 1):
           a, b = b, a + b
       return b
   ```

### Step 3: Main Program Structure
1. Create the main program structure
2. Implement user input handling
3. Display the Fibanocci Numbers

## Testing Instructions

Test both implementations with various inputs:
   - Small numbers (n < 10)
   - Medium numbers (10 ≤ n ≤ 30)
   - Large numbers (30 < n ≤ 40)

## Expected Output Format
```
Fibonacci Sequence Generator Comparison
-------------------------------------
Input number (n): 30

Sequence (first 10 numbers):
0, 1, 1, 2, 3, 5, 8, 13, 21, 34
```
