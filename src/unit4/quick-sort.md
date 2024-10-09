# Quick Sort

# 1. Concept

Quicksort is a highly efficient, divide-and-conquer sorting algorithm. It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays are then sorted recursively.

<iframe width="560" height="315" src="https://www.youtube.com/embed/Hoixgm4-P4M?si=DqyiIN_-7HelgK7w" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/WprjBK0p6rw?si=2jhorIKFSNkNu8A9" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

# 2. How Does Quicksort Work

Quicksort follows these steps:

1. Choose a pivot element from the array.
2. Partition the array:
   - Move all elements smaller than the pivot to its left.
   - Move all elements larger than the pivot to its right.
3. Recursively apply steps 1-2 to the sub-array of elements with smaller values and the sub-array of elements with larger values.

The base case of the recursion is arrays of size zero or one, which are always sorted.

# 3. Time / Space Complexity

Time Complexity:
- Worst-case: O(n²) - when the pivot is always the smallest or largest element
- Average-case: O(n log n)
- Best-case: O(n log n)

Space Complexity:
- Worst-case: O(n) - due to the recursive call stack
- Average-case: O(log n)

Note: The space complexity can be reduced to O(log n) by using tail recursion optimization.

# 4. When to Use & When Not to Use Quicksort

When to use:
- For large datasets where efficiency is crucial
- When average-case performance is more important than worst-case performance
- In situations where in-place sorting is beneficial to save memory
- When a good pivot selection strategy can be implemented

When not to use:
- When stability is required (preserving the relative order of equal elements)
- In systems where worst-case performance is critical
- For small datasets where simpler algorithms like insertion sort might be faster
- In memory-constrained environments where the recursive nature might be problematic

# 5. Implementing Quicksort in Python

Here's a Python implementation of the quicksort algorithm:

```python
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)
```

Note: This implementation is not in-place and uses extra space. An in-place version would be more memory-efficient but slightly more complex.

# 6. Scenario Problem and Solution

Problem: A teacher wants to rank students based on their total scores, which are calculated from multiple subjects. The scores need to be sorted in descending order to assign ranks.

Example:

```python
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x['total_score'] > pivot['total_score']]
        middle = [x for x in arr if x['total_score'] == pivot['total_score']]
        right = [x for x in arr if x['total_score'] < pivot['total_score']]
        return quicksort(left) + middle + quicksort(right)

# List of students with their names and total scores
students = [
    {"name": "Alice", "total_score": 385},
    {"name": "Bob", "total_score": 350},
    {"name": "Charlie", "total_score": 400},
    {"name": "David", "total_score": 395},
    {"name": "Eve", "total_score": 355}
]

print("Original order:")
for student in students:
    print(f"{student['name']}: {student['total_score']}")

sorted_students = quicksort(students)

print("\nRanked order:")
for rank, student in enumerate(sorted_students, 1):
    print(f"Rank {rank}: {student['name']} - {student['total_score']}")
```

Output:
```
Original order:
Alice: 385
Bob: 350
Charlie: 400
David: 395
Eve: 355

Ranked order:
Rank 1: Charlie - 400
Rank 2: David - 395
Rank 3: Alice - 385
Rank 4: Eve - 355
Rank 5: Bob - 350
```

This example demonstrates how quicksort can be used to efficiently rank students based on their total scores, sorting them in descending order.
