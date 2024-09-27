# Implement Stack using Queue(s) Problem

# Leetcode Lesson: Implement Stack using Queues

## 1. Problem Statement

Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (`push`, `pop`, `top`, `empty`).

Implement the `MyStack` class:
- `push(x)` Pushes element x to the top of the stack.
- `pop()` Removes the element on the top of the stack and returns it.
- `top()` Returns the element on the top of the stack.
- `empty()` Returns `true` if the stack is empty, `false` otherwise.

Notes:
- You must use only standard queue operations, which means only `push to back`, `peek/pop from front`, `size`, and `is empty` are valid.
- Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue), as long as you use only a queue's standard operations.

## 2. Conceptual Understanding

This problem challenges us to implement a stack (LIFO - Last In, First Out) data structure using only queue (FIFO - First In, First Out) operations. It's like trying to create a stack of plates (where you add and remove from the top) using only queues (where you add to the back and remove from the front).

The key is to find a way to reverse the order of elements when needed, as stacks and queues have opposite ordering principles.

## 3. Approach Brainstorming

We can consider two main approaches:
1. **Make push operation costly**: Keep the elements in the correct stack order, but make pushing a new element expensive.
2. **Make pop operation costly**: Allow pushing to be simple, but make popping an element more complex.

We'll focus on making the push operation costly, as it provides a more straightforward implementation for the other operations.

## 4. Optimal Solution Walkthrough

Here's how we can implement the stack using two queues:

1. Use two queues: `q1` and `q2`.
2. For `push` operation:
   - Add the new element to `q2`.
   - Move all elements from `q1` to `q2`.
   - Swap `q1` and `q2`.
3. For `pop`, `top`, and `empty` operations:
   - Perform these operations directly on `q1`.

This approach ensures that `q1` always has the elements in the correct stack order (newest on top).

## 5. Python Implementation

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

## 6. Time and Space Complexity Analysis

**Time Complexity**:
- `push`: O(n), where n is the number of elements in the stack
- `pop`: O(1)
- `top`: O(1)
- `empty`: O(1)

**Space Complexity**: O(n), where n is the number of elements in the stack

The push operation is costly in terms of time, but this allows other operations to be very efficient.

## 7. Edge Cases and Testing

Consider these test cases:
- Push multiple elements, then pop all
- Push, pop, push again
- Check top after multiple pushes
- Check empty on a new stack and after operations
- Push, pop, check empty, push again

## 8. Common Pitfalls and Mistakes

- Forgetting to swap queues after push operation
- Implementing pop or top incorrectly when the stack is empty
- Using list methods instead of queue methods

## 9. Optimization Opportunities

- We could use a single queue instead of two, rotating the queue after each push operation.
- If many consecutive push operations are expected, we could optimize by delaying the reordering until a pop or top operation is called.

## 10. Related Problems and Concepts

- "Implement Queue using Stacks" (reverse problem)
- Understanding of stack and queue data structures
- Adapter design pattern (adapting one interface to another)

## 11. Reflection Questions

1. How would the implementation change if we made the pop operation costly instead of push?
2. Can you think of a real-world scenario where you might need to implement a stack interface using queue-like operations?
3. How does this implementation compare to a native stack implementation in terms of efficiency?

## 12. Additional Resources

- [Python Queue documentation](https://docs.python.org/3/library/queue.html)
- [Stack data structure](https://en.wikipedia.org/wiki/Stack_(abstract_data_type))
- [Queue data structure](https://en.wikipedia.org/wiki/Queue_(abstract_data_type))
- [Adapter pattern](https://en.wikipedia.org/wiki/Adapter_pattern)
