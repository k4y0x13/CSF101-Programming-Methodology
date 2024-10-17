# Practical 8: Implementing Sorting Algorithms

## Objective
In this lab, you will implement three classic sorting algorithms: Bubble Sort, Merge Sort, and Quick Sort. This exercise will help you understand the mechanics of these algorithms and compare their performance.

## Prerequisites
- Basic knowledge of Python syntax
- Understanding of lists and functions in Python
- Familiarity with time complexity concepts (optional, but helpful)

## Lab Steps

### Step 1: Implement Bubble Sort

Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order.

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Test the function
test_arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(test_arr.copy())
print("Bubble Sort Result:", sorted_arr)
```

### Step 2: Implement Merge Sort

Merge Sort is a divide-and-conquer algorithm that divides the input array into two halves, recursively sorts them, and then merges the two sorted halves.

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Test the function
test_arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = merge_sort(test_arr)
print("Merge Sort Result:", sorted_arr)
```

### Step 3: Implement Quick Sort

Quick Sort is another divide-and-conquer algorithm that picks an element as a pivot and partitions the array around the pivot.

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

# Test the function
test_arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = quick_sort(test_arr)
print("Quick Sort Result:", sorted_arr)
```

### Step 4: Compare Performance

Now, let's create a function to compare the performance of these sorting algorithms:

```python
import time
import random

def compare_sorting_algorithms(arr):
    algorithms = [
        ("Bubble Sort", bubble_sort),
        ("Merge Sort", merge_sort),
        ("Quick Sort", quick_sort)
    ]
    
    for name, func in algorithms:
        arr_copy = arr.copy()
        start_time = time.time()
        func(arr_copy)
        end_time = time.time()
        print(f"{name} took {end_time - start_time:.6f} seconds")

# Generate a large random array
large_arr = [random.randint(1, 1000) for _ in range(1000)]

# Compare the algorithms
compare_sorting_algorithms(large_arr)
```

## Exercises for Students

1. Implement an in-place version of Quick Sort to improve its space efficiency.
2. Modify Bubble Sort to stop early if the list becomes sorted before all passes are complete.
3. Implement a hybrid sorting algorithm that uses Insertion Sort for small subarrays in Merge Sort or Quick Sort.
4. Create a visualization of how each sorting algorithm works using a library like Matplotlib.

## Conclusion

In this lab, you've implemented three classic sorting algorithms: Bubble Sort, Merge Sort, and Quick Sort. You've also compared their performance on a large random array. 

Key takeaways:
- Bubble Sort is simple but inefficient for large datasets (O(n^2) time complexity).
- Merge Sort provides stable, predictable performance (O(n log n) time complexity) but requires extra space.
- Quick Sort is often the fastest in practice (average O(n log n) time complexity) but can degrade to O(n^2) in worst cases.

Remember that the choice of sorting algorithm depends on the specific requirements of your application, such as the size and initial order of the data, memory constraints, and whether a stable sort is needed.
