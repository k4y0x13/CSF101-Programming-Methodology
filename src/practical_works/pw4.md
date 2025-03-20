# Practical 4: Implementing Stacks and Queues

## Objective
In this lab, you will implement stack and queue data structures in Python and use them to solve practical problems. This exercise will help you understand these fundamental data structures and their applications.

**Submission Date:** October 29th

## Prerequisites
- Basic knowledge of Python syntax
- Understanding of lists in Python
- Familiarity with classes in Python (optional, but helpful)

## Lab Steps

### Part 1: Implementing a Stack

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

### Part 2: Implementing a Queue

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

### Part 3: Solving Practical Problems

Now that we have implemented our stack and queue, let's use them to solve some practical problems.

#### Problem 1: Balanced Parentheses

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

#### Problem 2: Reverse a String

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

#### Problem 3: Hot Potato Simulation

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

## Exercises for Students

1. Implement a function that uses a stack to evaluate postfix expressions.
2. Create a function that uses two stacks to implement a queue.
3. Use a queue to implement a basic task scheduler that processes tasks in the order they were added.
4. Implement a function that uses a stack to convert infix expressions to postfix.

## Conclusion

In this lab, you've implemented stack and queue data structures in Python and used them to solve practical problems. These fundamental data structures are crucial in computer science and are used in various applications, from algorithm implementation to system design.

Remember to test your code with different inputs to ensure it works correctly in various scenarios. As you progress, try to think of other real-world problems that could be solved using stacks and queues.
