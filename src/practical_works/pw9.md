# Practical 9: Singly Linked List Implementation, Reverse Linked List, Merge Two Sorted Lists, Remove Nth Node From End of List

## Objective
In this lab, you will implement a singly linked list data structure in Python. You'll create basic operations and list manipulation functions, gaining a deeper understanding of linked data structures and their operations.

**Submission Date:** November 1st


## Prerequisites
- Basic knowledge of Python syntax
- Understanding of classes and object-oriented programming in Python
- Familiarity with data structures concepts

## Lab Steps

### Step 1: Define the Node Class

First, let's create a `Node` class to represent individual elements in our linked list:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

### Step 2: Create the LinkedList Class

Now, let's create the `LinkedList` class with a constructor:

```python
class LinkedList:
    def __init__(self):
        self.head = None
```

### Step 3: Implement the Append Method

Let's add a method to append nodes to the end of the list:

```python
class LinkedList:
    # ... (previous code)

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

# Test the append method
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
```

### Step 4: Implement the Display Method

Now, let's add a method to display the list contents:

```python
class LinkedList:
    # ... (previous code)

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))

# Test the display method
ll.display()  # Output: 1 -> 2 -> 3
```

### Step 5: Implement the Insert Method

Let's add a method to insert a node at a specific position:

```python
class LinkedList:
    # ... (previous code)

    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(position - 1):
            if current is None:
                raise IndexError("Position out of range")
            current = current.next
        new_node.next = current.next
        current.next = new_node

# Test the insert method
ll.insert(4, 1)
ll.display()  # Output: 1 -> 4 -> 2 -> 3
```

### Step 6: Implement the Delete Method

Now, let's implement a method to delete a node by its value:

```python
class LinkedList:
    # ... (previous code)

    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

# Test the delete method
ll.delete(2)
ll.display()  # Output: 1 -> 4 -> 3
```

### Step 7: Implement the Search Method

Let's add a method to search for a value in the list:

```python
class LinkedList:
    # ... (previous code)

    def search(self, data):
        current = self.head
        position = 0
        while current:
            if current.data == data:
                return position
            current = current.next
            position += 1
        return -1

# Test the search method
print(ll.search(4))  # Output: 1
print(ll.search(5))  # Output: -1
```

### Step 8: Implement the Reverse Method

Finally, let's add a method to reverse the linked list:

```python
class LinkedList:
    # ... (previous code)

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

# Test the reverse method
ll.reverse()
ll.display()  # Output: 3 -> 4 -> 1
```

## Exercises for Students

1. Implement a method to find the middle element of the linked list.
2. Create a method to detect if the linked list has a cycle.
3. Implement a method to remove duplicates from an unsorted linked list.
4. Add a method to merge two sorted linked lists into a single sorted linked list.

## Conclusion

In this lab, you've implemented a singly linked list in Python with various operations such as append, insert, delete, search, and reverse. You've practiced working with linked data structures and manipulating pointers.

Remember to test your implementation thoroughly with different scenarios to ensure it works correctly. Understanding linked lists is crucial for grasping more complex data structures and algorithms.
