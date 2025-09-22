# Bubble Sort


# 1. Concept

Bubble sort is a simple sorting algorithm that repeatedly steps through a list, compares adjacent elements, and swaps them if they are in the wrong order. The algorithm gets its name from the way smaller elements "bubble" to the top of the list with each iteration.

<iframe width="560" height="315" src="https://www.youtube.com/embed/xli_FI7CuzA?si=ycw7yauzQ_UmVhVR" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

# 2. How Does Bubble Sort Work

Bubble sort works by repeatedly traversing the list from left to right, comparing adjacent elements, and swapping them if they are in the wrong order. This process is repeated for each element in the list until no more swaps are needed, which indicates that the list is sorted.

The steps are as follows:
1. Start with the first element (index 0).
2. Compare the current element with the next element.
3. If the current element is greater than the next element, swap them.
4. Move to the next element and repeat steps 2-3 until the end of the list.
5. Repeat steps 1-4 for each element in the list.
6. The algorithm stops when no more swaps are performed in a full pass.

# 3. Time / Space Complexity

Time Complexity:
- Worst-case: O(n²) - when the array is in reverse order
- Average-case: O(n²)
- Best-case: O(n) - when the array is already sorted

Space Complexity:
- O(1) - Bubble sort is an **in-place** sorting algorithm, meaning it doesn't require any extra space proportional to the input size.

# 4. When to Use & When Not to Use Bubble Sort

When to use:
- For small datasets or nearly sorted lists
- When simplicity is preferred over efficiency
- In educational settings to teach basic sorting concepts
- When memory usage is a concern (due to its in-place nature)

When not to use:
- For large datasets (inefficient for big lists)
- In performance-critical applications
- When faster algorithms like QuickSort or MergeSort are available
- In production environments where efficiency is crucial

# 5. Implementing Bubble Sort in Python

Here's a Python implementation of the bubble sort algorithm:

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Flag to optimize the algorithm
        swapped = False
        
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        # If no swapping occurred, array is already sorted
        if not swapped:
            break
    
    return arr
```

# 6. Scenario Problem and Solution

Problem: A teacher has a list of student scores and wants to sort them in ascending order to determine the class ranking.

Example:

```python
def bubble_sort(scores):
    n = len(scores)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if scores[j] > scores[j+1]:
                scores[j], scores[j+1] = scores[j+1], scores[j]
                swapped = True
        if not swapped:
            break
    return scores

# List of student scores
student_scores = [78, 65, 90, 82, 70, 88, 85]

print("Original scores:", student_scores)
sorted_scores = bubble_sort(student_scores)
print("Sorted scores:", sorted_scores)

# Determine rankings
rankings = {score: rank for rank, score in enumerate(sorted(set(sorted_scores), reverse=True), 1)}
student_rankings = [rankings[score] for score in student_scores]

print("Student rankings:", student_rankings)
```

Output:
```
Original scores: [78, 65, 90, 82, 70, 88, 85]
Sorted scores: [65, 70, 78, 82, 85, 88, 90]
Student rankings: [5, 7, 1, 4, 6, 2, 3]
```
