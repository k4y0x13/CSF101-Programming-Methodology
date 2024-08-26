# Exercise

# Python Data Structures

These exercises are designed to help you practice working with various data structures in Python, including lists, stacks, queues, and deques. Follow each step carefully and try to predict the output before running the code.

## File Organization

We'll use the following file structure:

```
csf101-python_exercises/
└── data_structures/
    ├── arrays.py
    ├── multi_dimensional_arrays.py
    ├── lists.py
    ├── stacks.py
    ├── queues.py
    └── deques.py
```

You already have the `data_structures` directory. Create the new Python files (`lists.py`, `stacks.py`, `queues.py`, and `deques.py`) in this directory.

## Exercise 1: Working with Lists

File: `data_structures/lists.py`

1. Create a list of your favorite fruits.

   ```python
   fruits = ["apple", "banana", "cherry", "date"]
   print(fruits)
   ```

   Expected output: `['apple', 'banana', 'cherry', 'date']`

2. Add a new fruit to your list using the `append()` method.

   ```python
   fruits.append("elderberry")
   print(fruits)
   ```

   Expected output: `['apple', 'banana', 'cherry', 'date', 'elderberry']`

3. Insert a fruit at the beginning of the list using the `insert()` method.

   ```python
   fruits.insert(0, "fig")
   print(fruits)
   ```

   Expected output: `['fig', 'apple', 'banana', 'cherry', 'date', 'elderberry']`

4. Remove the third fruit from the list using the `pop()` method.

   ```python
   removed_fruit = fruits.pop(2)
   print(f"Removed fruit: {removed_fruit}")
   print(f"Updated list: {fruits}")
   ```

   Expected output:

   ```
   Removed fruit: banana
   Updated list: ['fig', 'apple', 'cherry', 'date', 'elderberry']
   ```

5. Find the index of a specific fruit using the `index()` method.

   ```python
   cherry_index = fruits.index("cherry")
   print(f"Index of 'cherry': {cherry_index}")
   ```

   Expected output: `Index of 'cherry': 2`

6. Count the occurrences of a fruit using the `count()` method.

   ```python
   fruits.append("apple")
   apple_count = fruits.count("apple")
   print(f"Number of 'apple's in the list: {apple_count}")
   ```

   Expected output: `Number of 'apple's in the list: 2`

7. Sort the list of fruits in alphabetical order.

   ```python
   fruits.sort()
   print(f"Sorted fruits: {fruits}")
   ```

   Expected output: `Sorted fruits: ['apple', 'apple', 'cherry', 'date', 'elderberry', 'fig']`

8. Reverse the order of the list.

   ```python
   fruits.reverse()
   print(f"Reversed fruits: {fruits}")
   ```

   Expected output: `Reversed fruits: ['fig', 'elderberry', 'date', 'cherry', 'apple', 'apple']`

9. Create a new list with unique fruits using a set.

   ```python
   unique_fruits = list(set(fruits))
   print(f"Unique fruits: {unique_fruits}")
   ```

   Expected output: `Unique fruits: ['fig', 'apple', 'date', 'cherry', 'elderberry']`

   Note: The order may vary due to set's unordered nature.

10. Try to remove a fruit that doesn't exist in the list.

    ```python
    try:
        fruits.remove("grape")
    except ValueError as e:
        print(f"Error: {e}")
    ```

    Expected output: `Error: list.remove(x): x not in list`

## Exercise 2: Working with Stacks

File: `data_structures/stacks.py`

11. Implement a stack using a Python list.

    ```python
    stack = []

    # Push elements onto the stack
    stack.append(1)
    stack.append(2)
    stack.append(3)

    print(f"Stack after pushing elements: {stack}")
    ```

    Expected output: `Stack after pushing elements: [1, 2, 3]`

12. Pop elements from the stack.

    ```python
    popped_item = stack.pop()
    print(f"Popped item: {popped_item}")
    print(f"Stack after popping: {stack}")
    ```

    Expected output:

    ```
    Popped item: 3
    Stack after popping: [1, 2]
    ```

13. Peek at the top element of the stack without removing it.

    ```python
    top_item = stack[-1]
    print(f"Top item (peek): {top_item}")
    print(f"Stack after peeking: {stack}")
    ```

    Expected output:

    ```
    Top item (peek): 2
    Stack after peeking: [1, 2]
    ```

14. Check if the stack is empty.

    ```python
    is_empty = len(stack) == 0
    print(f"Is the stack empty? {is_empty}")
    ```

    Expected output: `Is the stack empty? False`

15. Clear the stack and check if it's empty again.

    ```python
    stack.clear()
    is_empty = len(stack) == 0
    print(f"Is the stack empty after clearing? {is_empty}")
    ```

    Expected output: `Is the stack empty after clearing? True`

## Exercise 3: Working with Queues

File: `data_structures/queues.py`

16. Implement a queue using `collections.deque`.

    ```python
    from collections import deque

    queue = deque()

    # Enqueue elements
    queue.append("A")
    queue.append("B")
    queue.append("C")

    print(f"Queue after enqueuing elements: {queue}")
    ```

    Expected output: `Queue after enqueuing elements: deque(['A', 'B', 'C'])`

17. Dequeue elements from the queue.

    ```python
    dequeued_item = queue.popleft()
    print(f"Dequeued item: {dequeued_item}")
    print(f"Queue after dequeuing: {queue}")
    ```

    Expected output:

    ```
    Dequeued item: A
    Queue after dequeuing: deque(['B', 'C'])
    ```

18. Check if the queue is empty.

    ```python
    is_empty = len(queue) == 0
    print(f"Is the queue empty? {is_empty}")
    ```

    Expected output: `Is the queue empty? False`

19. Get the first element of the queue without removing it.

    ```python
    first_item = queue[0]
    print(f"First item (without removing): {first_item}")
    print(f"Queue after peeking: {queue}")
    ```

    Expected output:

    ```
    First item (without removing): B
    Queue after peeking: deque(['B', 'C'])
    ```

20. Add multiple elements to the queue at once.

    ```python
    queue.extend(["D", "E", "F"])
    print(f"Queue after adding multiple elements: {queue}")
    ```

    Expected output: `Queue after adding multiple elements: deque(['B', 'C', 'D', 'E', 'F'])`

## Exercise 4: Working with Deques

File: `data_structures/deques.py`

21. Implement a deque using `collections.deque`.

    ```python
    from collections import deque

    deque_obj = deque()

    # Add elements to both ends
    deque_obj.appendleft("A")
    deque_obj.append("B")
    deque_obj.appendleft("C")

    print(f"Deque after adding elements: {deque_obj}")
    ```

    Expected output: `Deque after adding elements: deque(['C', 'A', 'B'])`

22. Remove elements from both ends of the deque.

    ```python
    left_item = deque_obj.popleft()
    right_item = deque_obj.pop()

    print(f"Removed from left: {left_item}")
    print(f"Removed from right: {right_item}")
    print(f"Deque after removing elements: {deque_obj}")
    ```

    Expected output:

    ```
    Removed from left: C
    Removed from right: B
    Deque after removing elements: deque(['A'])
    ```

23. Rotate the deque.

    ```python
    # Add more elements
    deque_obj.extend(["D", "E", "F"])
    print(f"Deque before rotation: {deque_obj}")

    # Rotate to the right
    deque_obj.rotate(1)
    print(f"Deque after right rotation: {deque_obj}")

    # Rotate to the left
    deque_obj.rotate(-2)
    print(f"Deque after left rotation: {deque_obj}")
    ```

    Expected output:

    ```
    Deque before rotation: deque(['A', 'D', 'E', 'F'])
    Deque after right rotation: deque(['F', 'A', 'D', 'E'])
    Deque after left rotation: deque(['D', 'E', 'F', 'A'])
    ```

24. Count the occurrences of an element in the deque.

    ```python
    deque_obj.append("D")
    d_count = deque_obj.count("D")
    print(f"Number of 'D's in the deque: {d_count}")
    ```

    Expected output: `Number of 'D's in the deque: 2`

25. Create a new deque with a maximum length (maxlen).

    ```python
    limited_deque = deque(maxlen=3)
    limited_deque.extend([1, 2, 3])
    print(f"Limited deque: {limited_deque}")

    # Try to add one more element
    limited_deque.append(4)
    print(f"Limited deque after adding one more element: {limited_deque}")
    ```

    Expected output:

    ```
    Limited deque: deque([1, 2, 3], maxlen=3)
    Limited deque after adding one more element: deque([2, 3, 4], maxlen=3)
    ```

    Note: When a new element is added to a full deque with a maxlen, the first element is automatically removed.

## Final Notes

- These exercises cover a wide range of operations on lists, stacks, queues, and deques in Python.
- Remember that lists are **versatile** and can be _used to implement stacks_, but for queues and deques, it's more efficient to use `collections.deque`.
- Always be mindful of **potential errors** when working with these data structures, especially when trying to access or remove elements from empty structures.
- The `collections.deque` is a powerful and flexible data structure that can be used for both queues and deques, offering efficient operations at both ends.

Remember to run each file separately to see the output of your exercises. You can do this by navigating to the `data_structures` directory in your terminal and running `python filename.py` (e.g., `python lists.py`).

**Congratulations!**
