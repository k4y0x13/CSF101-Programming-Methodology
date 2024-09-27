# Merge Two Sorted Lists Problem

# Leetcode Lesson: Merge Two Sorted Lists

## 1. Problem Statement

You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

**Example 1:**
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

**Example 2:**
Input: list1 = [], list2 = []
Output: []

**Example 3:**
Input: list1 = [], list2 = [0]
Output: [0]

**Constraints:**
- The number of nodes in both lists is in the range [0, 50].
- -100 <= Node.val <= 100
- Both list1 and list2 are sorted in non-decreasing order.

## 2. Conceptual Understanding

This problem involves working with linked lists, a fundamental data structure in computer science. The task is to combine two already sorted linked lists into a single sorted linked list.

Think of it like merging two sorted piles of numbered cards into one sorted pile. You compare the top cards of each pile and always take the smaller one to add to your new pile.

## 3. Approach Brainstorming

Let's consider a few approaches:
1. **Create a new list**: Create a new linked list and add nodes from both lists in sorted order.
2. **In-place merge**: Modify the existing lists to merge them without creating new nodes.
3. **Recursive approach**: Solve the problem recursively, breaking it down into smaller subproblems.

Each approach has trade-offs in terms of time complexity, space complexity, and code simplicity.

## 4. Optimal Solution Walkthrough

We'll use the in-place merge approach as it's efficient and doesn't require extra space:

1. Create a dummy node as the start of our result list.
2. Use a pointer to keep track of where we're inserting nodes.
3. Iterate through both lists simultaneously:
   - Compare the current nodes of both lists.
   - Append the smaller node to our result list.
   - Move forward in the list we took the node from.
4. If one list is exhausted, append the remainder of the other list.
5. Return the next node after the dummy node (the actual head of our merged list).

This approach is optimal because it merges the lists in a single pass and doesn't create any new nodes.

## 5. Python Implementation

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    dummy = ListNode(0)
    current = dummy
    
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    if list1:
        current.next = list1
    if list2:
        current.next = list2
    
    return dummy.next
```

- We use a `dummy` node to simplify handling the head of the merged list.
- `current` keeps track of the last node in our merged list.
- We compare `list1.val` and `list2.val`, always choosing the smaller one.
- After the loop, we append any remaining nodes from either list.

## 6. Time and Space Complexity Analysis

**Time Complexity**: O(n + m)
- We iterate through both lists once, where n and m are the lengths of list1 and list2 respectively.

**Space Complexity**: O(1)
- We only use a constant amount of extra space (the dummy node and a few pointers), regardless of input size.

This solution optimizes both time and space complexity.

## 7. Edge Cases and Testing

Consider these test cases:
- `list1 = [1,2,3], list2 = [4,5,6]` (no interleaving)
- `list1 = [], list2 = [1,2,3]` (one list is empty)
- `list1 = [], list2 = []` (both lists are empty)
- `list1 = [1,1,1], list2 = [1,1,1]` (all elements are the same)

## 8. Common Pitfalls and Mistakes

- Forgetting to handle the case where one list is exhausted before the other.
- Incorrectly updating the `next` pointers, leading to cycles in the list.
- Modifying the input lists when it's not allowed (though in this problem it's typically fine).

## 9. Optimization Opportunities

Our solution is already quite optimal, but here are some situational optimizations:
- If we know one list is typically much shorter, we could check if it's empty first.
- In a language with manual memory management, we could potentially reuse nodes to save memory allocations.

## 10. Related Problems and Concepts

- "Merge K Sorted Lists" (an extension of this problem)
- "Sort List" (often uses merge sort, which involves merging)
- Linked List operations in general

## 11. Reflection Questions

1. How would this algorithm change if the lists were sorted in descending order?
2. Can you think of a recursive solution to this problem? How would its space complexity differ?
3. In what real-world scenarios might you need to merge sorted data structures?

## 12. Additional Resources

- [Python Linked Lists](https://realpython.com/linked-lists-python/)
- [Merge Sort Algorithm](https://en.wikipedia.org/wiki/Merge_sort) (uses a similar merging concept)
- [Time Complexity Analysis](https://wiki.python.org/moin/TimeComplexity)
