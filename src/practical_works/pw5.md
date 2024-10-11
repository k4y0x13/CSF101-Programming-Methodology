# Practical Work V

# Practical 5: Stack and Queue Data Structures
**Due Date:** [Specify date]
**Submission:** GitHub repository link containing:
- Python source code (.py files)
- Lab report in markdown format
- Test cases and results

## Learning Objectives
- Understand stack and queue data structures
- Implement basic operations for both structures
- Apply these structures to solve practical problems
- Practice object-oriented programming concepts

## Requirements
Create Python programs that:
1. Implement a Stack class with basic operations
2. Implement a Queue class with basic operations
3. Solve two practical problems:
   - Use Stack to check balanced parentheses in an expression
   - Use Queue to simulate a print job scheduler

## Step-by-Step Implementation Guide

### Part 1: Stack Implementation

#### Step 1: Create Basic Stack Class
1. Create a new file named `stack.py`
2. Implement the basic Stack class:
```python
class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
```

#### Step 2: Add Stack Operations
1. Add push operation:
```python
    def push(self, item):
        self.items.append(item)
        print(f"Pushed {item} to stack")
```

2. Add pop operation:
```python
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty")
            return None
```

3. Add peek operation:
```python
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is empty")
            return None
```

#### Step 3: Create Stack Test Program
1. Create test cases in `stack_test.py`:
```python
from stack import Stack

def test_stack():
    stack = Stack()
    
    # Test push operation
    stack.push(1)
    stack.push(2)
    stack.push(3)
    
    # Test peek operation
    print(f"Top item: {stack.peek()}")
    
    # Test pop operation
    print(f"Popped item: {stack.pop()}")
    print(f"New size: {stack.size()}")

if __name__ == "__main__":
    test_stack()
```

### Part 2: Queue Implementation

#### Step 1: Create Basic Queue Class
1. Create a new file named `queue.py`
2. Implement the basic Queue class:
```python
class Queue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
```

#### Step 2: Add Queue Operations
1. Add enqueue operation:
```python
    def enqueue(self, item):
        self.items.append(item)
        print(f"Enqueued {item} to queue")
```

2. Add dequeue operation:
```python
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Queue is empty")
            return None
```

3. Add front operation:
```python
    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("Queue is empty")
            return None
```

#### Step 3: Create Queue Test Program
1. Create test cases in `queue_test.py`:
```python
from queue import Queue

def test_queue():
    queue = Queue()
    
    # Test enqueue operation
    queue.enqueue("Task 1")
    queue.enqueue("Task 2")
    queue.enqueue("Task 3")
    
    # Test front operation
    print(f"Front item: {queue.front()}")
    
    # Test dequeue operation
    print(f"Dequeued item: {queue.dequeue()}")
    print(f"New size: {queue.size()}")

if __name__ == "__main__":
    test_queue()
```

### Part 3: Practical Applications

#### Application 1: Balanced Parentheses Checker
1. Create `parentheses_checker.py`:
```python
from stack import Stack

def check_balanced_parentheses(expression):
    stack = Stack()
    
    for char in expression:
        if char == '(':
            stack.push(char)
        elif char == ')':
            if stack.is_empty():
                return False
            stack.pop()
    
    return stack.is_empty()

# Test the function
expressions = [
    "(())",
    "(()",
    "())",
    "(()())",
]

for expr in expressions:
    result = check_balanced_parentheses(expr)
    print(f"Expression {expr} is {'balanced' if result else 'not balanced'}")
```

#### Application 2: Print Job Scheduler
1. Create `print_scheduler.py`:
```python
from queue import Queue
import time

class PrintJob:
    def __init__(self, document_name, num_pages):
        self.document_name = document_name
        self.num_pages = num_pages

class PrinterScheduler:
    def __init__(self):
        self.print_queue = Queue()
    
    def add_print_job(self, document_name, num_pages):
        job = PrintJob(document_name, num_pages)
        self.print_queue.enqueue(job)
        print(f"Added print job: {document_name}")
    
    def process_print_jobs(self):
        while not self.print_queue.is_empty():
            job = self.print_queue.dequeue()
            print(f"Printing {job.document_name}")
            print(f"Pages to print: {job.num_pages}")
            # Simulate printing time
            time.sleep(1)
            print(f"Finished printing {job.document_name}")

# Test the printer scheduler
scheduler = PrinterScheduler()
scheduler.add_print_job("Document1.pdf", 5)
scheduler.add_print_job("Document2.pdf", 3)
scheduler.add_print_job("Document3.pdf", 7)
scheduler.process_print_jobs()
```

## Testing Instructions
1. Test Stack Implementation:
   - Run `stack_test.py`
   - Verify all stack operations work correctly
   - Test edge cases (empty stack, full stack)

2. Test Queue Implementation:
   - Run `queue_test.py`
   - Verify all queue operations work correctly
   - Test edge cases (empty queue, full queue)

3. Test Practical Applications:
   - Run `parentheses_checker.py` with different expressions
   - Run `print_scheduler.py` with various print jobs

## Expected Output Format
### Stack Operations
```
Pushed 1 to stack
Pushed 2 to stack
Pushed 3 to stack
Top item: 3
Popped item: 3
New size: 2
```

### Queue Operations
```
Enqueued Task 1 to queue
Enqueued Task 2 to queue
Enqueued Task 3 to queue
Front item: Task 1
Dequeued item: Task 1
New size: 2
```

## Grading Criteria Breakdown
### Executability (3 points)
- Stack implementation works correctly (1)
- Queue implementation works correctly (1)
- Practical applications run without errors (1)

### Instruction Compliance (2 points)
- All required classes and methods implemented (1)
- Proper file structure and naming conventions (1)

### Solution Approach (2 points)
- Efficient implementation of data structures (1)
- Proper error handling (1)

### Data Structure Usage (2 points)
- Correct implementation of stack and queue operations (1)
- Appropriate use in practical applications (1)

### Submission Timeliness (1 point)
- Submitted before deadline on GitHub (1)

## Submission Requirements
1. In your `ProgrammingPracticals` repository, create a folder named `Practical5`
2. Submit the following files:
   - `stack.py`
   - `queue.py`
   - `stack_test.py`
   - `queue_test.py`
   - `parentheses_checker.py`
   - `print_scheduler.py`
   - `lab_report.md`

## Lab Report Template
Your lab report should include:
1. Introduction to stacks and queues
2. Implementation approach for each data structure
3. Explanation of practical applications
4. Test cases and results
5. Challenges faced and solutions
6. Conclusions and learning outcomes

## Additional Resources
- Python list operations
- Time complexity of operations
- Object-oriented programming in Python
- Real-world applications of stacks and queues
