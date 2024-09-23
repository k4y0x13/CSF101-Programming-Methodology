# Remove Nth Node from end of list problem

# Leetcode Lesson: Remove Nth Node From End of List

## 1. Problem Statement

Given the head of a linked list, remove the nth node from the end of the list and return its head.

**Example 1:**
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

**Example 2:**
Input: head = [1], n = 1
Output: []

**Example 3:**
Input: head = [1,2], n = 1
Output: [1]

**Constraints:**
- The number of nodes in the list is sz.
- 1 <= sz <= 30
- 0 <= Node.val <= 100
- 1 <= n <= sz

## 2. Conceptual Understanding

This problem involves manipulating a linked list, which is a linear data structure where elements are stored in nodes. Each node contains a data field and a reference (or link) to the next node in the sequence.

The challenge here is to remove a node from a specific position, counting from the end of the list. This requires us to think about how to traverse the list and keep track of positions relative to the end.

## 3. Approach Brainstorming

Let's consider a few approaches:
1. **Two-pass algorithm**: First pass to count the nodes, second to remove the nth node.
2. **One-pass algorithm with two pointers**: Use two pointers with a gap of n between them.
3. **Recursive approach**: Use the call stack to keep track of position from the end.

Each approach has trade-offs in terms of time complexity, space complexity, and code simplicity.

## 4. Optimal Solution Walkthrough

We'll use the one-pass algorithm with two pointers, as it's efficient and doesn't require extra space:

1. Initialize two pointers, `fast` and `slow`, to the head of the list.
2. Move `fast` n nodes ahead.
3. If `fast` is null, it means we need to remove the head. Return `head.next`.
4. Move both `fast` and `slow` until `fast` reaches the last node.
5. Now, `slow` is just before the node we want to remove.
6. Update `slow.next` to skip the next node (effectively removing it).
7. Return the head of the modified list.

This approach is optimal because it solves the problem in one pass and uses constant extra space.

## 5. Python Implementation

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(0)
    dummy.next = head
    fast = slow = dummy
    
    # Move fast pointer n nodes ahead
    for _ in range(n):
        fast = fast.next
    
    # Move both pointers until fast reaches the end
    while fast.next:
        fast = fast.next
        slow = slow.next
    
    # Remove the nth node
    slow.next = slow.next.next
    
    return dummy.next
```

- We use a `dummy` node to handle the case where we need to remove the head.
- `fast` and `slow` are our two pointers.
- We move `fast` n nodes ahead, then move both until `fast` reaches the end.
- Finally, we update `slow.next` to skip (and thus remove) the nth node from the end.

## 6. Time and Space Complexity Analysis

**Time Complexity**: O(L), where L is the length of the list
- We traverse the list once, so it's linear time.

**Space Complexity**: O(1)
- We only use a constant amount of extra space (the two pointers), regardless of the input size.

## 7. Edge Cases and Testing

Consider these test cases:
- `[1,2,3,4,5]`, n = 2 (removing from the middle)
- `[1]`, n = 1 (removing the only node)
- `[1,2]`, n = 2 (removing the head)
- `[1,2,3]`, n = 3 (removing the head)
- `[1,2,3]`, n = 1 (removing the tail)

## 8. Common Pitfalls and Mistakes

- Forgetting to handle the case where the head needs to be removed.
- Off-by-one errors in counting nodes.
- Not considering empty list input (though not required by the problem constraints).
- Modifying the head directly without using a dummy node, which can complicate the solution.

## 9. Optimization Opportunities

Our solution is already quite optimal, but here are some situational optimizations:
- If we frequently remove nodes from linked lists, we might consider a doubly linked list for O(1) removal at the cost of extra space.
- In a language with manual memory management, we'd need to free the memory of the removed node.

## 10. Related Problems and Concepts

- "Reverse Linked List"
- "Middle of the Linked List"
- Two-pointer technique in linked list problems
- Floyd's Cycle-Finding Algorithm (not directly related, but another important linked list technique)

## 11. Reflection Questions

1. How would you solve this problem if you couldn't use extra space at all (not even for the dummy node)?
2. Can you think of a real-world scenario where removing an item from the end of a sequence is important?
3. How would you modify this solution to remove the nth node from the beginning instead?

## 12. Additional Resources

- [Python Linked Lists](https://realpython.com/linked-lists-python/)
- [Two Pointer Technique](https://leetcode.com/articles/two-pointer-technique/)
- [Linked List Data Structure](https://en.wikipedia.org/wiki/Linked_list)
