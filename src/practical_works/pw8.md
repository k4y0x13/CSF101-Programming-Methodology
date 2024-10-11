# Practical Work VII

# Practical 8: Sorting Algorithms Implementation
**Due Date:** [Specify date]
**Submission:** GitHub repository link containing:
- Python source code (.py file)
- Lab report in markdown format
- Test data files

## Learning Objectives
- Understand and implement three fundamental sorting algorithms
- Compare the performance of different sorting techniques
- Practice array manipulation
- Learn algorithm complexity through practical implementation
- Implement proper testing and validation

## Requirements
Create a Python program that implements three sorting algorithms:
1. Bubble Sort
2. Merge Sort
3. Quick Sort

The program should:
- Allow user to input arrays or read from file
- Display the step-by-step sorting process
- Show the execution time for each algorithm
- Compare results between algorithms

## Step-by-Step Implementation Guide

### Step 1: Basic Setup and Utility Functions
1. Create a new Python file named `sorting_algorithms.py`
2. Import required modules:
```python
import time
import random

def print_step(arr, step_num, algorithm_name):
    print(f"{algorithm_name} - Step {step_num}: {arr}")

def generate_random_array(size, min_val=1, max_val=100):
    return [random.randint(min_val, max_val) for _ in range(size)]
```

### Step 2: Bubble Sort Implementation
1. Implement basic bubble sort:
```python
def bubble_sort(arr, show_steps=False):
    n = len(arr)
    steps = 0
    
    # Make a copy to avoid modifying original array
    arr_copy = arr.copy()
    
    for i in range(n):
        # Flag to optimize if array is already sorted
        swapped = False
        
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if arr_copy[j] > arr_copy[j + 1]:
                # Swap them if they are in wrong order
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
                swapped = True
                
                if show_steps:
                    steps += 1
                    print_step(arr_copy, steps, "Bubble Sort")
        
        # If no swapping occurred, array is already sorted
        if not swapped:
            break
            
    return arr_copy
```

### Step 3: Merge Sort Implementation
1. Implement merge sort with two functions:
```python
def merge(left, right, show_steps=False, steps=0):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    if show_steps:
        steps += 1
        print_step(result, steps, "Merge Sort - Merging")
    
    return result

def merge_sort(arr, show_steps=False, steps=0):
    if len(arr) <= 1:
        return arr
        
    mid = len(arr) // 2
    
    if show_steps:
        print(f"Splitting array into: {arr[:mid]} and {arr[mid:]}")
    
    left = merge_sort(arr[:mid], show_steps, steps)
    right = merge_sort(arr[mid:], show_steps, steps)
    
    return merge(left, right, show_steps, steps)
```

### Step 4: Quick Sort Implementation
1. Implement quick sort:
```python
def quick_sort(arr, show_steps=False, steps=0):
    def partition(low, high):
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                
                if show_steps:
                    nonlocal steps
                    steps += 1
                    print_step(arr, steps, "Quick Sort")
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    def quick_sort_helper(low, high):
        if low < high:
            pi = partition(low, high)
            quick_sort_helper(low, pi - 1)
            quick_sort_helper(pi + 1, high)
    
    # Make a copy to avoid modifying original array
    arr_copy = arr.copy()
    quick_sort_helper(0, len(arr_copy) - 1)
    return arr_copy
```

### Step 5: Main Program Implementation
1. Create the main program structure:
```python
def main():
    # Get input choice from user
    print("Choose input method:")
    print("1. Manual input")
    print("2. Random array generation")
    print("3. Read from file")
    
    choice = input("Enter your choice (1-3): ")
    
    # Get array based on user choice
    if choice == '1':
        nums = input("Enter numbers separated by space: ")
        arr = [int(x) for x in nums.split()]
    elif choice == '2':
        size = int(input("Enter array size: "))
        arr = generate_random_array(size)
    else:
        filename = input("Enter file name: ")
        with open(filename, 'r') as f:
            arr = [int(x) for x in f.read().split()]
    
    # Show original array
    print("\nOriginal array:", arr)
    
    # Sort using all three algorithms and measure time
    for sort_func in [bubble_sort, merge_sort, quick_sort]:
        start_time = time.time()
        sorted_arr = sort_func(arr.copy(), show_steps=True)
        end_time = time.time()
        
        print(f"\n{sort_func.__name__} result: {sorted_arr}")
        print(f"Time taken: {end_time - start_time:.6f} seconds")

if __name__ == "__main__":
    main()
```

## Testing Instructions
1. Create test cases:
   - Small array (5-10 elements)
   - Medium array (50-100 elements)
   - Large array (500-1000 elements)
   - Already sorted array
   - Reverse sorted array
   - Array with duplicate elements

2. Test each sorting algorithm with:
   ```python
   # Example test cases
   test_arrays = [
       [64, 34, 25, 12, 22, 11, 90],  # Small array
       [1, 2, 3, 4, 5],               # Already sorted
       [5, 4, 3, 2, 1],               # Reverse sorted
       [1, 1, 2, 2, 3, 3]             # Duplicates
   ]
   ```

## Expected Output Format
```
Original Array: [64, 34, 25, 12, 22, 11, 90]

Bubble Sort Steps:
Step 1: [34, 64, 25, 12, 22, 11, 90]
Step 2: [34, 25, 64, 12, 22, 11, 90]
...
Final: [11, 12, 22, 25, 34, 64, 90]
Time taken: X.XXXXXX seconds

Merge Sort Steps:
Splitting array into: [64, 34, 25] and [12, 22, 11, 90]
...
Final: [11, 12, 22, 25, 34, 64, 90]
Time taken: X.XXXXXX seconds

Quick Sort Steps:
Step 1: [64, 34, 25, 12, 22, 11, 90]
...
Final: [11, 12, 22, 25, 34, 64, 90]
Time taken: X.XXXXXX seconds
```

## Grading Criteria Breakdown
### Executability (3 points)
- All three algorithms work correctly (1.5)
- Proper handling of different input methods (1.5)

### Instruction Compliance (2 points)
- All required functions implemented (1)
- Proper step-by-step visualization (1)

### Solution Approach (2 points)
- Correct implementation of algorithms (1)
- Proper error handling (1)

### Data Structure Usage (2 points)
- Efficient array manipulation (1)
- Proper use of recursive/iterative approaches (1)

### Submission Timeliness (1 point)
- Submitted before deadline on GitHub (1)

## Submission Requirements
1. In your GitHub repository `ProgrammingPracticals`:
   - `sorting_algorithms.py`
   - `lab_report.md`
   - Test data files
   - README.md with setup and usage instructions

## Lab Report Template
Your lab report should include:
1. Introduction to sorting algorithms
2. Implementation approach for each algorithm
3. Complexity analysis (Big O notation)
4. Performance comparison
5. Test cases and results
6. Conclusions and learning outcomes

## Additional Resources
- Time complexity analysis of sorting algorithms
- Python list operations
- Recursive vs iterative approaches
- Visualization tools for sorting algorithms
