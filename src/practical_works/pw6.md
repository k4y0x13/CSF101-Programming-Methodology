# Practical Work VI

# Practical 6: Singly Linked List Implementation
**Due Date:** [Specify date]
**Submission:** GitHub repository link containing:
- Python source code (.py file)
- Lab report in markdown format
- Test cases file

## Learning Objectives
- Understand linked list data structure concepts
- Implement basic linked list operations
- Practice object-oriented programming
- Learn list manipulation techniques
- Develop debugging skills

## Requirements
Create a Python program that implements a singly linked list with the following operations:
1. Insert node at beginning
2. Insert node at end
3. Insert node at specific position
4. Delete node from beginning
5. Delete node from end
6. Delete node from specific position
7. Search for a value
8. Display the list
9. Count total nodes
10. Reverse the list

## Step-by-Step Implementation Guide

### Step 1: Create Node Class
1. Create a new Python file named `linked_list.py`
2. Implement the Node class:
```python
class Node:
    def __init__(self, data):
        self.data = data    # Store the data
        self.next = None    # Initialize next pointer as null
```

### Step 2: Create LinkedList Class
1. Implement the basic LinkedList class:
```python
class LinkedList:
    def __init__(self):
        self.head = None    # Initialize head as null
```

### Step 3: Display Function
1. Implement list display functionality:
```python
def display(self):
    if self.head is None:
        print("List is empty")
        return
        
    current = self.head
    while current is not None:
        print(current.data, end=" -> ")
        current = current.next
    print("None")
```

### Step 4: Insert at Beginning
1. Implement insertion at the start of list:
```python
def insert_at_beginning(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node
```

### Step 5: Insert at End
1. Implement insertion at the end of list:
```python
def insert_at_end(self, data):
    new_node = Node(data)
    
    if self.head is None:
        self.head = new_node
        return
        
    current = self.head
    while current.next is not None:
        current = current.next
    current.next = new_node
```

### Step 6: Insert at Position
1. Implement insertion at specific position:
```python
def insert_at_position(self, position, data):
    if position < 0:
        print("Invalid position")
        return
        
    if position == 0:
        self.insert_at_beginning(data)
        return
        
    new_node = Node(data)
    current = self.head
    for i in range(position - 1):
        if current is None:
            print("Position out of range")
            return
        current = current.next
        
    new_node.next = current.next
    current.next = new_node
```

### Step 7: Delete from Beginning
1. Implement deletion from start:
```python
def delete_from_beginning(self):
    if self.head is None:
        print("List is empty")
        return
        
    self.head = self.head.next
```

### Step 8: Delete from End
1. Implement deletion from end:
```python
def delete_from_end(self):
    if self.head is None:
        print("List is empty")
        return
        
    if self.head.next is None:
        self.head = None
        return
        
    current = self.head
    while current.next.next is not None:
        current = current.next
    current.next = None
```

### Step 9: Search Function
1. Implement search functionality:
```python
def search(self, value):
    current = self.head
    position = 0
    while current is not None:
        if current.data == value:
            return position
        current = current.next
        position += 1
    return -1
```

### Step 10: Count Nodes
1. Implement node counting:
```python
def count_nodes(self):
    count = 0
    current = self.head
    while current is not None:
        count += 1
        current = current.next
    return count
```

### Step 11: Reverse List
1. Implement list reversal:
```python
def reverse_list(self):
    previous = None
    current = self.head
    while current is not None:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node
    self.head = previous
```

### Step 12: Main Program
1. Create a main program to test all operations:
```python
def main():
    # Create a new linked list
    my_list = LinkedList()
    
    while True:
        print("\nLinked List Operations:")
        print("1. Insert at beginning")
        print("2. Insert at end")
        print("3. Insert at position")
        print("4. Delete from beginning")
        print("5. Delete from end")
        print("6. Search value")
        print("7. Display list")
        print("8. Count nodes")
        print("9. Reverse list")
        print("10. Exit")
        
        choice = input("Enter your choice (1-10): ")
        
        # Add appropriate if-elif statements for each choice
        # Include error handling for user inputs

if __name__ == "__main__":
    main()
```

## Testing Instructions
1. Test each operation individually:
   - Create an empty list
   - Insert several elements
   - Try all deletion operations
   - Search for existing and non-existing values
   - Test boundary conditions (empty list, single node)

2. Test Cases to Cover:
   - Empty list operations
   - Single node operations
   - Multiple node operations
   - Invalid inputs
   - Boundary conditions

## Expected Output Format
```
Linked List Operations:
1. Insert at beginning
2. Insert at end
3. Insert at position
4. Delete from beginning
5. Delete from end
6. Search value
7. Display list
8. Count nodes
9. Reverse list
10. Exit

Current List: 10 -> 20 -> 30 -> 40 -> None
Number of nodes: 4
```

## Grading Criteria Breakdown
### Executability (3 points)
- Program runs without errors (1.5)
- All operations work correctly (1.5)

### Instruction Compliance (2 points)
- All required functions implemented (1)
- Proper code structure and documentation (1)

### Solution Approach (2 points)
- Efficient implementation (1)
- Proper error handling (1)

### Data Structure Usage (2 points)
- Correct linked list implementation (1)
- Proper node connections and updates (1)

### Submission Timeliness (1 point)
- Submitted before deadline on GitHub (1)

## Submission Requirements
1. In your `ProgrammingPracticals` repository, create a folder named `Practical7`
2. Submit the following files:
   - `linked_list.py`
   - `test_cases.py` (containing test scenarios)
   - `lab_report.md`
3. Update README.md with:
   - Implementation details
   - Usage instructions
   - Test case descriptions

## Lab Report Template
Your lab report should include:
1. Introduction to linked lists
2. Implementation approach
3. Challenges faced and solutions
4. Test cases and results
5. Conclusions and learning outcomes

## Additional Resources
- Python object-oriented programming
- Linked list visualization tools
- Common linked list interview questions
- Time complexity analysis of operations
