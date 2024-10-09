# Practical Work IV

# Practical 4: Search Algorithms
**Due Date:** 

## Objective
Create a program that implements both linear and binary search algorithms to find numbers in a list.

## Step-by-Step Implementation

### Step 1: Create Basic Program Structure
Create a new file named `search_algorithms.py` and set up the basic structure:

```python
def main():
    # Our test list
    numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    
    # Value we want to find
    target = 7
    
    print("List of numbers:", numbers)
    print("We want to find:", target)

if __name__ == "__main__":
    main()
```

Run this code to make sure it works. It should print the list and target number.

### Step 2: Implement Linear Search
Add the linear search function:

```python
def linear_search(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i    # Return position if found
    return -1          # Return -1 if not found

def main():
    numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = 7
    
    print("List of numbers:", numbers)
    print("We want to find:", target)
    
    # Try linear search
    result = linear_search(numbers, target)
    if result != -1:
        print(f"Linear Search: Found {target} at position {result}")
    else:
        print(f"Linear Search: {target} not found in the list")

if __name__ == "__main__":
    main()
```

Test this code. It should find and print the position of the target number.

### Step 3: Implement Binary Search
Add the binary search function:

```python
def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1
    
    while left <= right:
        middle = (left + right) // 2
        
        # If we found the number
        if numbers[middle] == target:
            return middle
        
        # If target is smaller, ignore right half
        elif numbers[middle] > target:
            right = middle - 1
        
        # If target is larger, ignore left half
        else:
            left = middle + 1
            
    return -1    # Not found

def main():
    numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = 7
    
    print("List of numbers:", numbers)
    print("We want to find:", target)
    
    # Try linear search
    linear_result = linear_search(numbers, target)
    if linear_result != -1:
        print(f"Linear Search: Found {target} at position {linear_result}")
    else:
        print(f"Linear Search: {target} not found in the list")
        
    # Try binary search
    binary_result = binary_search(numbers, target)
    if binary_result != -1:
        print(f"Binary Search: Found {target} at position {binary_result}")
    else:
        print(f"Binary Search: {target} not found in the list")

if __name__ == "__main__":
    main()
```

### Step 4: Add User Input
Modify the main function to accept user input:

```python
def main():
    # Create our test list
    numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    
    while True:
        # Show the menu
        print("\nSearch Algorithms Test")
        print("List of numbers:", numbers)
        
        # Get target number from user
        try:
            target = int(input("\nEnter a number to search for (or -1 to quit): "))
            if target == -1:
                break
                
            # Try linear search
            linear_result = linear_search(numbers, target)
            if linear_result != -1:
                print(f"Linear Search: Found {target} at position {linear_result}")
            else:
                print(f"Linear Search: {target} not found in the list")
                
            # Try binary search
            binary_result = binary_search(numbers, target)
            if binary_result != -1:
                print(f"Binary Search: Found {target} at position {binary_result}")
            else:
                print(f"Binary Search: {target} not found in the list")
                
        except ValueError:
            print("Please enter a valid number")

if __name__ == "__main__":
    main()
```

### Step 5: Test Your Program
Test your program with these cases:
1. Find number 7 (exists in list)
2. Find number 10 (doesn't exist in list)
3. Find number 1 (first element)
4. Find number 19 (last element)
5. Enter invalid input (like "abc")

## Extra Challenge (Optional)
If you want to try more:
1. Add a feature to let users input their own list of numbers
2. Add a counter to show how many comparisons each search method makes
3. Add a timer to measure how long each search takes
