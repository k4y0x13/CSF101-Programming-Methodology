# Tower of Hanoi Problem

# Leetcode Lesson: Tower of Hanoi

## 1. Problem Statement

The Tower of Hanoi is a classic problem in computer science and mathematics. The problem setup is as follows:

- There are three rods and a number of disks of different sizes which can slide onto any rod.
- The puzzle starts with the disks neatly stacked in ascending order of size on one rod, the smallest disk at the top.
- The objective of the puzzle is to move the entire stack to another rod, obeying the following rules:
  1. Only one disk can be moved at a time.
  2. Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod.
  3. No larger disk may be placed on top of a smaller disk.

Your task is to write a function that prints out the series of moves required to solve the Tower of Hanoi puzzle for n disks.

**Example:**
Input: n = 3 (number of disks)
Output: 
```
Move disk 1 from rod A to rod C
Move disk 2 from rod A to rod B
Move disk 1 from rod C to rod B
Move disk 3 from rod A to rod C
Move disk 1 from rod B to rod A
Move disk 2 from rod B to rod C
Move disk 1 from rod A to rod C
```

## 2. Conceptual Understanding

The Tower of Hanoi problem is an excellent example of a problem that can be solved using recursion. The key insight is that to move n disks:

1. Move n-1 disks from the source to the auxiliary rod.
2. Move the largest disk from the source to the destination rod.
3. Move the n-1 disks from the auxiliary rod to the destination rod.

This process is recursive because moving n-1 disks involves the same process with a smaller number of disks.

Think of it like unpacking nested boxes. You need to unpack the smaller boxes (move smaller disks) before you can move the largest box (disk).

## 3. Approach Brainstorming

While the recursive approach is the most common and elegant solution, let's consider a few approaches:

1. **Recursive**: Use the natural recursive structure of the problem.
2. **Iterative**: Use a loop and a stack to simulate the recursion.
3. **Mathematical**: Use the mathematical formula for the optimal moves (less intuitive but interesting for discussion).

We'll focus on the recursive approach as it's the most intuitive and commonly used for this problem.

## 4. Optimal Solution Walkthrough

The recursive solution follows these steps:

1. Base case: If there's only one disk, move it directly from the source to the destination.
2. Recursive case:
   a. Move n-1 disks from source to auxiliary rod.
   b. Move the nth disk from source to destination.
   c. Move n-1 disks from auxiliary to destination.

This approach elegantly solves the problem by breaking it down into smaller, manageable subproblems.

## 5. Python Implementation

```python
def tower_of_hanoi(n, source, destination, auxiliary):
    if n == 1:
        print(f"Move disk 1 from rod {source} to rod {destination}")
        return
    tower_of_hanoi(n-1, source, auxiliary, destination)
    print(f"Move disk {n} from rod {source} to rod {destination}")
    tower_of_hanoi(n-1, auxiliary, destination, source)

# Example usage
n = 3
tower_of_hanoi(n, 'A', 'C', 'B')
```

- The function takes four parameters: the number of disks `n`, and the names of the source, destination, and auxiliary rods.
- The base case (n == 1) simply moves the disk and returns.
- For n > 1, we recursively move n-1 disks, then move the nth disk, then recursively move the n-1 disks again.

## 6. Time and Space Complexity Analysis

**Time Complexity**: O(2^n)
- Each call to `tower_of_hanoi` makes two recursive calls, except for the base case.
- The recursion depth is n, so we have 2^n - 1 function calls.

**Space Complexity**: O(n)
- The space complexity is determined by the maximum depth of the recursion stack, which is n.

This exponential time complexity shows why the problem becomes quickly intractable for large n.

## 7. Edge Cases and Testing

Consider these test cases:
- n = 1 (base case)
- n = 2 (simplest case with multiple moves)
- n = 3 (as in the example)
- n = 0 (invalid input, should be handled)

## 8. Common Pitfalls and Mistakes

- Forgetting the base case, leading to infinite recursion.
- Mixing up the order of the auxiliary and destination rods in recursive calls.
- Not handling invalid inputs (e.g., negative number of disks).

## 9. Optimization Opportunities

The recursive solution is already optimal in terms of the number of moves. However:
- We could modify it to return a list of moves instead of printing them.
- For very large n, we might consider using an iterative solution to avoid stack overflow.

## 10. Related Problems and Concepts

- Recursion in general
- Other recursive problems like Fibonacci sequence, factorial calculation
- Stack data structure (for understanding the recursive calls)
- Dynamic programming (for more complex variations of the problem)

## 11. Reflection Questions

1. How would you modify the solution to count the number of moves without printing them?
2. Can you think of a real-world scenario where a similar recursive strategy might be useful?
3. How would the solution change if there were four rods instead of three?

## 12. Additional Resources

- [Visualization of Tower of Hanoi](https://www.mathsisfun.com/games/towerofhanoi.html)
- [Recursion in Python](https://realpython.com/python-thinking-recursively/)
- [Time Complexity Analysis of Recursive Algorithms](https://www.geeksforgeeks.org/time-complexity-recursive-algorithms/)
