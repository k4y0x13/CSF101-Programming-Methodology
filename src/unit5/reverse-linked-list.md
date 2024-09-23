# Reverse Linked List Problem

# Leetcode Lesson: Reverse Linked List

## 1. Problem Statement

Given the `head` of a singly linked list, reverse the list, and return the reversed list.

**Example 1:**
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

**Example 2:**
Input: head = [1,2]
Output: [2,1]

**Example 3:**
Input: head = []
Output: []

**Constraints:**
- The number of nodes in the list is the range [0, 5000].
- -5000 <= Node.val <= 5000

## 2. Conceptual Understanding

A linked list is a data structure where each element (node) contains a value and a reference (or link) to the next node in the sequence. Reversing a linked list means changing these links so that each node points to its previous node instead of its next node.

Imagine a chain where each link is holding hands with the next link. To reverse it, we need to make each link let go of the hand it's holding and grab the hand of the link behind it instead.

## 3. Approach Brainstorming

Let's consider a few approaches:
1. **Iterative**: Traverse the list once, changing links as we go.
2. **Recursive**: Reverse the rest of the list, then add the first element at the end.
3. **Stack-based**: Use a stack to store nodes, then rebuild the list in reverse order.

Each approach has trade-offs in terms of time complexity, space complexity, and ease of understanding.

## 4. Optimal Solution Walkthrough

We'll focus on the iterative approach as it's often the most intuitive and efficient:

1. Initialize three pointers: `prev` as None, `current` as the head of the list, and `next` as None.
2. Traverse the list:
   - Save the next node.
   - Reverse the current node's pointer to point to the previous node.
   - Move `prev` and `current` one step forward.
3. Return `prev` as the new head of the reversed list.

This approach allows us to reverse the list in a single pass, changing links as we go.

## 5. Python Implementation

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    prev = None
    current = head
    
    while current is not None:
        next_temp = current.next  # Store next node
        current.next = prev       # Reverse the link
        prev = current            # Move prev one step
        current = next_temp       # Move current one step
    
    return prev  # prev is the new head of the reversed list
```

- We define a `ListNode` class to represent each node in the linked list.
- The `reverseList` function takes the head of the list and returns the new head of the reversed list.
- We use three pointers: `prev`, `current`, and `next_temp` to manage the reversal process.

## 6. Time and Space Complexity Analysis

**Time Complexity**: O(n)
- We traverse the list once, where n is the number of nodes in the list.

**Space Complexity**: O(1)
- We only use a constant amount of extra space (three pointers) regardless of the input size.

This solution optimizes both time and space complexity.

## 7. Edge Cases and Testing

Consider these test cases:
- `[]` (empty list)
- `[1]` (single node)
- `[1,2]` (two nodes)
- `[1,2,3,4,5]` (odd number of nodes)
- `[1,2,3,4]` (even number of nodes)

## 8. Common Pitfalls and Mistakes

- Forgetting to update the `next` pointer of the last node (which should point to `None`).
- Not handling the case of an empty list or a single-node list.
- Losing the reference to the rest of the list by not storing the `next` node before reversing the current link.

## 9. Optimization Opportunities

Our iterative solution is already quite optimal in terms of time and space complexity. However, here are some situational optimizations:
- If we know we're always dealing with short lists, a recursive solution might be more readable.
- In languages with tail-call optimization, a carefully written recursive solution could have the same space complexity as the iterative one.

## 10. Related Problems and Concepts

- "Reverse Linked List II" (reverse a portion of the linked list)
- "Palindrome Linked List" (uses the concept of reversing a linked list)
- Understanding pointers and memory management in general

## 11. Reflection Questions

1. How would you verify if your reversed list is correct?
2. Can you think of a real-world scenario where reversing a linked structure might be useful?
3. How would this solution change if we were dealing with a doubly linked list?

## 12. Additional Resources

- [Python Linked Lists](https://realpython.com/linked-lists-python/)
- [Visualizing Linked List Reversal](https://visualgo.net/en/list)
- [Recursion in Python](https://realpython.com/python-thinking-recursively/)
