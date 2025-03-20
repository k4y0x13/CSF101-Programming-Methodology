# Practical 5: Implementing Linear and Binary Search Algorithms

## Objective
In this lab, you will implement both linear and binary search algorithms in Python. You'll learn about the differences between these search methods, their time complexities, and when to use each one. This exercise will help you practice algorithm implementation, list manipulation, and control structures in Python.

**Submission Date:** October 29th

## Prerequisites
- Basic knowledge of Python syntax
- Understanding of lists and functions in Python
- Familiarity with control structures (if statements, loops)

## Lab Steps

### Step 1: Implement Linear Search

Let's start by implementing the linear search algorithm:

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if the target is found
    return -1  # Return -1 if the target is not in the list

# Test the function
test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
result = linear_search(test_list, 6)
print(f"Linear Search: Index of 6 is {result}")
```

### Step 2: Implement Binary Search

Now, let's implement the binary search algorithm. Remember, binary search requires a sorted list:

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Return the index if the target is found
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Return -1 if the target is not in the list

# Test the function
test_list_sorted = sorted(test_list)
result = binary_search(test_list_sorted, 6)
print(f"Binary Search: Index of 6 in sorted list is {result}")
```

### Step 3: Compare Performance

Let's create a function to compare the performance of both search algorithms:

```python
import time

def compare_search_algorithms(arr, target):
    # Linear Search
    start_time = time.time()
    linear_result = linear_search(arr, target)
    linear_time = time.time() - start_time
    
    # Binary Search (on sorted array)
    arr_sorted = sorted(arr)
    start_time = time.time()
    binary_result = binary_search(arr_sorted, target)
    binary_time = time.time() - start_time
    
    print(f"Linear Search: Found at index {linear_result}, Time: {linear_time:.6f} seconds")
    print(f"Binary Search: Found at index {binary_result}, Time: {binary_time:.6f} seconds")

# Test with a larger list
large_list = list(range(10000))
compare_search_algorithms(large_list, 8888)
```

### Step 4: Implement Recursive Binary Search

Let's also implement a recursive version of binary search:

```python
def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1
    
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

# Test the recursive function
result = binary_search_recursive(test_list_sorted, 6, 0, len(test_list_sorted) - 1)
print(f"Recursive Binary Search: Index of 6 in sorted list is {result}")
```

### Step 5: Create a Main Function

Finally, let's create a main function that demonstrates all our search algorithms:

```python
def main():
    # Create a list of 20 random integers between 1 and 100
    import random
    test_list = [random.randint(1, 100) for _ in range(20)]
    
    print("Original list:", test_list)
    print("Sorted list:", sorted(test_list))
    
    target = random.choice(test_list)  # Choose a random target from the list
    print(f"\nSearching for: {target}")
    
    # Linear Search
    result = linear_search(test_list, target)
    print(f"Linear Search: Found at index {result}")
    
    # Binary Search (iterative)
    sorted_list = sorted(test_list)
    result = binary_search(sorted_list, target)
    print(f"Binary Search (iterative): Found at index {result}")
    
    # Binary Search (recursive)
    result = binary_search_recursive(sorted_list, target, 0, len(sorted_list) - 1)
    print(f"Binary Search (recursive): Found at index {result}")
    
    # Compare performance
    print("\nPerformance Comparison:")
    compare_search_algorithms(list(range(100000)), 99999)

if __name__ == "__main__":
    main()
```

## Exercises for Students

1. Modify the linear search function to return all indices where the target appears, not just the first one.
2. Implement a function that uses binary search to find the insertion point for a target value in a sorted list.
3. Create a function that counts the number of comparisons made in each search algorithm.
4. Implement a jump search algorithm and compare its performance with linear and binary search.

## Conclusion

In this lab, you've implemented both linear and binary search algorithms in Python. You've learned about their differences, time complexities, and when to use each one. The modular approach we've taken allows for easy testing and comparison of these algorithms.

Remember that while binary search is generally faster for large sorted lists, it requires the list to be sorted first. Linear search, although slower for large lists, works on unsorted lists and can be more efficient for small lists or when searching for multiple occurrences of an element.
