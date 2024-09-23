# Contains Duplicate Problem

# Leetcode Lesson: Contains Duplicate

## 1. Problem Statement

Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

**Example 1:**
Input: nums = [1,2,3,1]
Output: true

**Example 2:**
Input: nums = [1,2,3,4]
Output: false

**Example 3:**
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

**Constraints:**
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9

## 2. Conceptual Understanding

This problem is essentially asking us to check for duplicates in an array. We need to determine if there's at least one number that appears more than once. 

Think of it like a group of people in a room. We're trying to find out if there are any twins (duplicate numbers) present.

## 3. Approach Brainstorming

Let's consider a few approaches:
1. **Brute Force**: Check every number against every other number.
2. **Sorting**: Sort the array and check adjacent elements.
3. **Hash Set**: Use a set to keep track of numbers we've seen.

Each approach has trade-offs in terms of time and space complexity.

## 4. Optimal Solution Walkthrough

The most efficient solution uses a hash set:

1. Create an empty set to store numbers we've seen.
2. Iterate through the array.
3. For each number:
   - If it's already in the set, we've found a duplicate. Return True.
   - If not, add it to the set.
4. If we finish the loop without finding duplicates, return False.

This approach is optimal because it allows us to check for duplicates in a single pass through the array.

## 5. Python Implementation

```python
def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
```

- We use a `set` called `seen` to store numbers we've encountered.
- The `in` operator checks if a number is in the set, which is a very fast operation.
- `seen.add(num)` adds a number to the set.

## 6. Time and Space Complexity Analysis

**Time Complexity**: O(n)
- We iterate through the array once, and each set operation (checking and adding) is O(1) on average.

**Space Complexity**: O(n)
- In the worst case, we might need to store all n elements in our set (if there are no duplicates).

This solution optimizes for time complexity at the cost of some additional space.

## 7. Edge Cases and Testing

Consider these test cases:
- `[1,2,3,4]` (no duplicates)
- `[1,1]` (duplicate at the beginning)
- `[1,2,3,1]` (duplicate at the end)
- `[]` (empty array)
- `[1,1,1,1,1]` (all elements are the same)

## 8. Common Pitfalls and Mistakes

- Forgetting to return `False` if the loop completes without finding duplicates.
- Using a list instead of a set, which would make the `in` operation slower.
- Modifying the input array (e.g., by sorting it) which might not be allowed in some contexts.

## 9. Optimization Opportunities

Our solution is already quite optimal, but here are some situational optimizations:
- If we know the range of numbers is small, we could use a boolean array instead of a set.
- We could potentially stop early if we've seen more than half of the possible numbers.

## 10. Related Problems and Concepts

- "Two Sum" problem (using a hash map)
- "Find the Duplicate Number" (more constrained version of this problem)
- Hash tables and sets in general

## 11. Reflection Questions

1. How would you solve this problem if you couldn't use extra space?
2. Can you think of a real-world scenario where checking for duplicates is important?
3. How would the solution change if we needed to find and return all duplicates?

## 12. Additional Resources

- [Python Set Operations](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset)
- [Time Complexity of Python Operations](https://wiki.python.org/moin/TimeComplexity)
- [Hash Table Data Structure](https://en.wikipedia.org/wiki/Hash_table)
