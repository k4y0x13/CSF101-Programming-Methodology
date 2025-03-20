# Practical 6b: Algorithms Backtracking and Recursions Exercises

## Objective
In this lab, you will implement backtracking and recursion exercises. This exercise will help you understand the mechanics of these algorithms and compare their performance.

**Submission Date:** November 4st

## Prerequisites
- Basic knowledge of Python syntax
- Understanding of lists and functions in Python
- Familiarity with time complexity concepts (optional, but helpful)

## Lab Steps
## Step 1: Implement a Recursive Fibonacci Generator
### First, let's create a recursive function to generate Fibonacci numbers:

```python
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Test the function
for i in range(10):
    print(f"F({i}) = {fibonacci_recursive(i)}")
```

### Step 2: Implement an Iterative Fibonacci Generator

Now, let's create an iterative function to generate Fibonacci numbers:

```python
def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Test the function
for i in range(10):
    print(f"F({i}) = {fibonacci_iterative(i)}")
```

### Step 3: Compare Performance

Let's create a function to measure the execution time of both approaches:

```python
import time

def measure_time(func, n):
    start = time.time()
    result = func(n)
    end = time.time()
    return result, end - start

# Test both functions and compare their execution times
n = 30
recursive_result, recursive_time = measure_time(fibonacci_recursive, n)
iterative_result, iterative_time = measure_time(fibonacci_iterative, n)

print(f"Recursive: F({n}) = {recursive_result}, Time: {recursive_time:.6f} seconds")
print(f"Iterative: F({n}) = {iterative_result}, Time: {iterative_time:.6f} seconds")
```

### Step 4: Implement a Generator Function for Fibonacci Sequence

Now, let's create a generator function that yields Fibonacci numbers:

```python
def fibonacci_generator(limit):
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1

# Test the generator
for i, fib in enumerate(fibonacci_generator(10)):
    print(f"F({i}) = {fib}")
```

### Step 5: Implement Memoization for Recursive Fibonacci

To improve the performance of the recursive approach, let's implement memoization:

```python
def fibonacci_memoized(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memoized(n-1, memo) + fibonacci_memoized(n-2, memo)
    return memo[n]

# Test the memoized function
for i in range(10):
    print(f"F({i}) = {fibonacci_memoized(i)}")

# Compare performance with the original recursive function
n = 30
memoized_result, memoized_time = measure_time(fibonacci_memoized, n)
print(f"Memoized: F({n}) = {memoized_result}, Time: {memoized_time:.6f} seconds")
```

## Exercises for Students

1. Modify the iterative function to return a list of Fibonacci numbers up to n, instead of just the nth number.
2. Implement a function that finds the index of the first Fibonacci number that exceeds a given value.
3. Create a function that determines if a given number is a Fibonacci number.
4. Implement a function that calculates the ratio between consecutive Fibonacci numbers and observe how it approaches the golden ratio.

## Discussion Questions

1. What are the advantages and disadvantages of the recursive approach compared to the iterative approach?
2. How does memoization improve the performance of the recursive function? Are there any drawbacks?
3. In what scenarios might you prefer to use a generator function over other implementations?
4. How does the space complexity differ between these implementations?

## Conclusion

In this lab, you've implemented multiple approaches to generate Fibonacci sequences in Python. You've explored recursive, iterative, and generator-based solutions, as well as an optimization technique (memoization). By comparing these approaches, you can gain insights into algorithm design, performance optimization, and the trade-offs between different implementation strategies.

Key takeaways:
- 

