# Practical 8: Implementing Stacks and Queues, including leetcode problems to Implement Stack using Queue(s), and Valid Parentheses

## Objective
In this lab, you will implement stack and queue data structures in Python and use them to solve practical problems. This exercise will help you understand these fundamental data structures and their applications.

**Submission Date:** October 29th

## Prerequisites
- Basic knowledge of Python syntax
- Understanding of lists in Python
- Familiarity with classes in Python (optional, but helpful)

## Part 1: Implementing a Stack

A stack is a Last-In-First-Out (LIFO) data structure. Let's implement a basic stack class:

```python
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")

    def size(self):
        return len(self.items)

# Test the Stack
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())  # Should print 3
print(stack.peek())  # Should print 2
print(stack.size())  # Should print 2
```

## Part 2: Implementing a Queue

A queue is a First-In-First-Out (FIFO) data structure. Let's implement a basic queue class:

```python
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty")

    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty")

    def size(self):
        return len(self.items)

# Test the Queue
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  # Should print 1
print(queue.front())  # Should print 2
print(queue.size())  # Should print 2
```

## Part 3: Leetcode Lesson: Implementing Stack Using Queue

### 1. Problem Statement

Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (`push`, `pop`, `top`, `empty`).

Implement the `MyStack` class:
- `push(x)` Pushes element x to the top of the stack.
- `pop()` Removes the element on the top of the stack and returns it.
- `top()` Returns the element on the top of the stack.
- `empty()` Returns `true` if the stack is empty, `false` otherwise.

Notes:
- You must use only standard queue operations, which means only `push to back`, `peek/pop from front`, `size`, and `is empty` are valid.
- Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue), as long as you use only a queue's standard operations.

### 2. Conceptual Understanding

This problem challenges us to implement a stack (LIFO - Last In, First Out) data structure using only queue (FIFO - First In, First Out) operations. It's like trying to create a stack of plates (where you add and remove from the top) using only queues (where you add to the back and remove from the front).

The key is to find a way to reverse the order of elements when needed, as stacks and queues have opposite ordering principles.

Here's how we can implement the stack using two queues:

1. Use two queues: `q1` and `q2`.
2. For `push` operation:
   - Add the new element to `q2`.
   - Move all elements from `q1` to `q2`.
   - Swap `q1` and `q2`.
3. For `pop`, `top`, and `empty` operations:
   - Perform these operations directly on `q1`.

This approach ensures that `q1` always has the elements in the correct stack order (newest on top).

### 3. Python Implementation

```python
from queue import Queue

class MyStack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x: int) -> None:
        self.q2.put(x)
        while not self.q1.empty():
            self.q2.put(self.q1.get())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q1.get()

    def top(self) -> int:
        return self.q1.queue[0]

    def empty(self) -> bool:
        return self.q1.empty()
```

- We use Python's `Queue` class for our queues.
- `push` adds the new element to `q2`, moves all elements from `q1` to `q2`, then swaps `q1` and `q2`.
- `pop` and `top` operate directly on `q1`.
- `empty` checks if `q1` is empty.

# Solving Practical Problems: Now that we have implemented our stack and queue, let's use them to solve some practical problems.

## Part 4 Problem: Reverse a String

Use a stack to reverse a string:

```python
def reverse_string(s):
    stack = Stack()
    for char in s:
        stack.push(char)
    
    reversed_string = ""
    while not stack.is_empty():
        reversed_string += stack.pop()
    
    return reversed_string

# Test the function
print(reverse_string("Hello, World!"))  # Should print "!dlroW ,olleH"
```

## Part 5 Problem: Hot Potato Simulation

Use a queue to simulate the Hot Potato game:

```python
def hot_potato(names, num):
    queue = Queue()
    for name in names:
        queue.enqueue(name)
    
    while queue.size() > 1:
        for _ in range(num):
            queue.enqueue(queue.dequeue())
        queue.dequeue()
    
    return queue.dequeue()

# Test the function
names = ["Bill", "David", "Susan", "Jane", "Kent", "Brad"]
print(hot_potato(names, 7))  # The winner's name will be printed
```

## Part 6 Problem: Balanced Parentheses

Use a stack to check if a string of parentheses is balanced:

```python
def is_balanced(parentheses):
    stack = Stack()
    for p in parentheses:
        if p == '(':
            stack.push(p)
        elif p == ')':
            if stack.is_empty():
                return False
            stack.pop()
    return stack.is_empty()

# Test the function
print(is_balanced("((()))"))  # Should print True
print(is_balanced("(()"))  # Should print False
```

## Part 7 Leetcode Lesson: Valid Parentheses

### 1. Problem Statement

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

**Example 1:**
Input: s = "()"
Output: true

**Example 2:**
Input: s = "()[]{}"
Output: true

**Example 3:**
Input: s = "(]"
Output: false

**Constraints:**
- 1 <= s.length <= 10^4
- `s` consists of parentheses only `'()[]{}'`

### 2. Conceptual Understanding

This problem is about validating the structure of nested parentheses. It's similar to checking if HTML tags or code blocks are properly nested and closed.

Think of it like nesting dolls: each smaller doll (inner parenthesis) needs to be completely enclosed by its larger doll (outer parenthesis) of the same type.

We'll use a stack-based approach:

1. Initialize an empty stack.
2. Iterate through each character in the string:
   - If it's an opening bracket, push it onto the stack.
   - If it's a closing bracket:
     - If the stack is empty, return False (no matching opening bracket).
     - If the top of the stack doesn't match the current closing bracket, return False.
     - If it matches, pop the top element from the stack.
3. After the loop, return True if the stack is empty, False otherwise.

This approach ensures that brackets are closed in the correct order and that every closing bracket has a matching opening bracket.

### 3. Python Implementation

```python
def isValid(s: str) -> bool:
    stack = []
    bracket_map = {")": "(", "}": "{", "]": "["}
    
    for char in s:
        if char in bracket_map:  # it's a closing bracket
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()
        else:  # it's an opening bracket
            stack.append(char)
    
    return len(stack) == 0
```

- We use a list `stack` to simulate a stack data structure.
- `bracket_map` is a dictionary that maps closing brackets to their corresponding opening brackets.
- `stack[-1]` accesses the top element of the stack.
- `stack.pop()` removes and returns the top element of the stack.
- `stack.append(char)` adds an element to the top of the stack.


## Further Exercises for Students

1. Implement a function that uses a stack to evaluate postfix expressions.
2. Create a function that uses two stacks to implement a queue.
3. Use a queue to implement a basic task scheduler that processes tasks in the order they were added.
4. Implement a function that uses a stack to convert infix expressions to postfix.

## Conclusion

In this lab, you've implemented stack and queue data structures in Python and used them to solve practical problems. These fundamental data structures are crucial in computer science and are used in various applications, from algorithm implementation to system design.

Remember to test your code with different inputs to ensure it works correctly in various scenarios. As you progress, try to think of other real-world problems that could be solved using stacks and queues.
