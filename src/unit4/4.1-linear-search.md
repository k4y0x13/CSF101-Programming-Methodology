# Linear Search Algorithm

# 1. Concept

Linear search, also known as **sequential search**, is one of the simplest searching algorithms. It works by sequentially checking each element in a collection until a match is found or the entire collection has been searched.

<iframe width="560" height="315" src="https://www.youtube.com/embed/19hcyQN8J7o?si=_EJnkgO8V6KJcVL6" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

# 2. How Linear Search Works

The algorithm follows these steps:
1. Start from the first element of the array.
2. Compare the current element with the target value.
3. If the current element matches the target, return its index.
4. If not, move to the next element.
5. Repeat steps 2-4 until the element is found or the end of the array is reached.
6. If the element is not found, return a signal (often -1) or False to indicate the element is not in the array.

**HOMEWORK:**
1. Draw a flowchart for Linear Search algorithm
2. Write Psuedocode for Linear Search algorithm

# 3. Time and Space Complexity

## Time Complexity
- Best Case: O(1) - when the target element is at the beginning of the array
- Worst Case: O(n) - when the target element is at the end or not in the array
- Average Case: O(n) - on average, we might need to search half the array

## Space Complexity
- O(1) - linear search uses a constant amount of extra space regardless of input size

# 4. When to Use & When Not to Use Linear Search

## Use Linear Search When:
- The array is small
- The array is unsorted
- You need to search for an element only once
- Simplicity is more important than speed
- Hardware constraints favor simple algorithms

## Avoid Linear Search When:
- The array is large and sorted (use binary search instead)
- You need to perform multiple searches on the same array (consider sorting first)
- Performance is critical and the dataset is large

# 5. Implementing Linear Search in Python

One of the implementation in Python: 

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if the element is found
    return -1  # Return -1 if the element is not found

# Example usage
my_array = [5, 2, 9, 1, 7, 6, 3]
result = linear_search(my_array, 7)
print(f"Element found at index: {result}")
```

# 6. Example Problem and Solution

## Problem Statement
A teacher has a list of student IDs and needs to find if a particular student is present in the class. Write a function that takes a list of student IDs and a target ID, and returns whether the student is present and their position in the list (1-indexed).

## Solution

```python
def find_student(student_ids, target_id):
    for i, student_id in enumerate(student_ids, start=1):
        if student_id == target_id:
            return f"Student with ID {target_id} is present at position {i}."
    return f"Student with ID {target_id} is not present in the class."

# Example usage
class_ids = [1001, 1002, 1003, 1004, 1005, 1006, 1007]
target_student = 1005

result = find_student(class_ids, target_student)
print(result)

# Test with a student not in the class
missing_student = 1010
result = find_student(class_ids, missing_student)
print(result)
```

This implementation uses linear search to find the student ID in the list. It returns the position (1-indexed for easier understanding by non-programmers) if the student is found, or a message indicating the student is not present.

The time complexity remains O(n) in the worst case, where n is the number of students in the class. This approach is suitable for small to medium-sized classes where the simplicity of implementation outweighs the need for optimized search performance.
