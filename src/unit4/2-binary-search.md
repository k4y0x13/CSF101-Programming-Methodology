# Binary Search

# 1. Concept

Binary search is a **highly efficient** searching algorithm used to find a specific element within a sorted array. It works on the principle of **divide and conquer**, repeatedly dividing the search interval in half until the desired element is found or it's determined that the element doesn't exist in the array.

# 2. How Binary Search Works

1. Start with a sorted array.
2. Define two pointers: `left` (starting at the first element) and `right` (starting at the last element).
3. Calculate the middle index: `mid = (left + right) // 2`.
4. Compare the middle element with the target value:
   - If equal, the search is successful.
   - If the target is less than the middle element, search the left half (set `right = mid - 1`).
   - If the target is greater than the middle element, search the right half (set `left = mid + 1`).
5. Repeat steps 3-4 until the element is found or the search space is exhausted (`left > right`).

# 3. Time and Space Complexity

- **Time Complexity**: 
  - Best case: O(1) - when the middle element is the target
  - Average case: O(log n)
  - Worst case: O(log n)
- **Space Complexity**: O(1) - constant space is used

The logarithmic time complexity makes binary search significantly faster than linear search for large datasets.

# 4. When to Use & When Not to Use Binary Search

**Use Binary Search when:**
- The array is sorted
- The array is large, and efficiency is crucial

**Don't Use Binary Search when:**
- The array is unsorted (sorting first may be costlier than a linear search)
- The array is small (linear search might be faster due to simplicity)
- The array is frequently modified (maintaining sorted order can be expensive)
- You need to find all occurrences of an element (binary search finds only one)

# 5. Implementing Binary Search in Python

Implementation in Python:

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Target found, return its index
        elif arr[mid] < target:
            left = mid + 1  # Target is in the right half
        else:
            right = mid - 1  # Target is in the left half

    return -1  # Target not found
```

# 6. Example Scenario: Finding a Student's Score

## Problem Statement

**Problem**: A school maintains a sorted list of student scores. Given a student's score, find their rank in the class (assuming no two students have the same score).

## Solution

```python
def find_rank(scores, target_score):
    left, right = 0, len(scores) - 1

    while left <= right:
        mid = (left + right) // 2
        if scores[mid] == target_score:
            return len(scores) - mid  # Rank is position from the end
        elif scores[mid] < target_score:
            right = mid - 1  # Look in the left half (higher scores)
        else:
            left = mid + 1  # Look in the right half (lower scores)

    # If the exact score isn't found, return the rank it would have
    return len(scores) - right

# Example usage
scores = [95, 90, 85, 80, 75, 70, 65, 60]  # Sorted in descending order
student_score = 82

rank = find_rank(scores, student_score)
print(f"A student with a score of {student_score} would rank {rank} in the class.")
```

In this example, we use binary search to efficiently find where a given score would fit in the sorted list of scores. The rank is determined by the position from the end of the list, as higher scores typically indicate better ranks.

This implementation showcases how binary search can be adapted to solve real-world problems efficiently, especially when dealing with sorted data.
