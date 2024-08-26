# Exercise

# Linked Data Structures using collections.deque

These exercises are designed to help you practice working with linked data structures in Python using the `collections.deque` class. Follow each step carefully and try to predict the output before running the code.

## File Organization

Use the following file structure:

```
csf101-python_exercises/
└── data_structures/
    ├── arrays.py
    ├── multi_dimensional_arrays.py
    └── linked_structures.py
```

Create a new file called `linked_structures.py` in the `data_structures` directory and complete the following exercises in this file.

## Exercises

1. Import the `deque` class from the `collections` module.

   ```python
   from collections import deque
   ```

2. Create an empty deque and print it.

   ```python
   my_list = deque()
   print(my_list)
   ```

   Expected output: `deque([])`

3. Add elements to the front of the deque using `appendleft()`.

   ```python
   my_list.appendleft(3)
   my_list.appendleft(2)
   my_list.appendleft(1)
   print(my_list)
   ```

   Expected output: `deque([1, 2, 3])`

4. Add elements to the back of the deque using `append()`.

   ```python
   my_list.append(4)
   my_list.append(5)
   print(my_list)
   ```

   Expected output: `deque([1, 2, 3, 4, 5])`

5. Remove and print an element from the front of the deque using `popleft()`.

   ```python
   front_element = my_list.popleft()
   print(f"Removed from front: {front_element}")
   print(my_list)
   ```

   Expected output:

   ```
   Removed from front: 1
   deque([2, 3, 4, 5])
   ```

6. Remove and print an element from the back of the deque using `pop()`.

   ```python
   back_element = my_list.pop()
   print(f"Removed from back: {back_element}")
   print(my_list)
   ```

   Expected output:

   ```
   Removed from back: 5
   deque([2, 3, 4])
   ```

7. Write a function to check if the deque is empty.

   ```python
   def is_empty(d):
       return len(d) == 0

   print(f"Is the deque empty? {is_empty(my_list)}")
   ```

   Expected output: `Is the deque empty? False`

8. Write a function to print all elements in the deque.

   ```python
   def print_deque(d):
       print(" -> ".join(map(str, d)) + " -> None")

   print_deque(my_list)
   ```

   Expected output: `2 -> 3 -> 4 -> None`

9. Implement a function to insert an element at a specific index in the deque.

   ```python
   def insert_at(d, index, item):
       temp = list(d)
       temp.insert(index, item)
       return deque(temp)

   my_list = insert_at(my_list, 1, 10)
   print_deque(my_list)
   ```

   Expected output: `2 -> 10 -> 3 -> 4 -> None`

10. Implement a function to remove the first occurrence of a specific element.

    ```python
    def remove_first(d, item):
        try:
            d.remove(item)
        except ValueError:
            print(f"{item} not found in the deque")

    remove_first(my_list, 3)
    print_deque(my_list)
    ```

    Expected output: `2 -> 10 -> 4 -> None`

11. Create a function to reverse the order of elements in the deque.

    ```python
    def reverse_deque(d):
        return deque(reversed(d))

    my_list = reverse_deque(my_list)
    print_deque(my_list)
    ```

    Expected output: `4 -> 10 -> 2 -> None`

12. Implement a function to find the index of a specific element in the deque.

    ```python
    def find_index(d, item):
        try:
            return list(d).index(item)
        except ValueError:
            return -1

    print(f"Index of 10: {find_index(my_list, 10)}")
    print(f"Index of 5: {find_index(my_list, 5)}")
    ```

    Expected output:

    ```
    Index of 10: 1
    Index of 5: -1
    ```

13. Create a function to count the occurrences of a specific element in the deque.

    ```python
    def count_occurrences(d, item):
        return list(d).count(item)

    my_list.append(4)
    print(f"Occurrences of 4: {count_occurrences(my_list, 4)}")
    ```

    Expected output: `Occurrences of 4: 2`

14. Implement a function to rotate the deque to the right by n positions.

    ```python
    def rotate_right(d, n):
        d.rotate(n)

    rotate_right(my_list, 2)
    print_deque(my_list)
    ```

    Expected output: `10 -> 2 -> 4 -> 4 -> None`

15. Create a function to check if a deque is a palindrome.

    ```python
    def is_palindrome(d):
        return list(d) == list(reversed(d))

    palindrome_deque = deque("racecar")
    print(f"Is 'racecar' a palindrome? {is_palindrome(palindrome_deque)}")
    print(f"Is our list a palindrome? {is_palindrome(my_list)}")
    ```

    Expected output:

    ```
    Is 'racecar' a palindrome? True
    Is our list a palindrome? False
    ```

16. Implement a function to merge two deques alternately.

    ```python
    def merge_alternate(d1, d2):
        result = deque()
        while d1 and d2:
            result.append(d1.popleft())
            result.append(d2.popleft())
        result.extend(d1)
        result.extend(d2)
        return result

    deque1 = deque([1, 3, 5])
    deque2 = deque([2, 4, 6])
    merged = merge_alternate(deque1, deque2)
    print_deque(merged)
    ```

    Expected output: `1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None`

17. Create a function to remove duplicates from a deque while preserving the original order.

    ```python
    def remove_duplicates(d):
        seen = set()
        return deque(x for x in d if not (x in seen or seen.add(x)))

    dup_deque = deque([1, 2, 2, 3, 4, 3, 5])
    no_dups = remove_duplicates(dup_deque)
    print_deque(no_dups)
    ```

    Expected output: `1 -> 2 -> 3 -> 4 -> 5 -> None`

18. Implement a function to find the maximum element in the deque.

    ```python
    def find_max(d):
        return max(d) if d else None

    print(f"Maximum element: {find_max(my_list)}")
    ```

    Expected output: `Maximum element: 10`

19. Create a function to split a deque into two halves.

    ```python
    def split_deque(d):
        mid = len(d) // 2
        return deque(list(d)[:mid]), deque(list(d)[mid:])

    left, right = split_deque(my_list)
    print("Left half:", end=" ")
    print_deque(left)
    print("Right half:", end=" ")
    print_deque(right)
    ```

    Expected output:

    ```
    Left half: 10 -> 2 -> None
    Right half: 4 -> 4 -> None
    ```

20. Implement a function to simulate a circular buffer using a deque with a maximum size.

    ```python
    def create_circular_buffer(size):
        return deque(maxlen=size)

    def add_to_buffer(buffer, item):
        buffer.append(item)

    circular_buffer = create_circular_buffer(3)
    for i in range(5):
        add_to_buffer(circular_buffer, i)
        print(f"Added {i}: {list(circular_buffer)}")
    ```

    Expected output:

    ```
    Added 0: [0]
    Added 1: [0, 1]
    Added 2: [0, 1, 2]
    Added 3: [1, 2, 3]
    Added 4: [2, 3, 4]
    ```

    Note: When the buffer is full, adding a new item removes the oldest item.

## Final Notes

- These exercises demonstrate various operations and use cases for `collections.deque` as a linked list-like structure.
- Remember that while deque allows O(1) operations at both ends, accessing or modifying elements in the middle is still O(n).
- Always consider the trade-offs between using a deque and other data structures like lists or custom linked list implementations.

Remember to run your `linked_structures.py` file to see the output of your exercises. You can do this by navigating to the `data_structures` directory in your terminal and running `python linked_structures.py`.
