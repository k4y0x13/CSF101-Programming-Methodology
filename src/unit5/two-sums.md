# Two Sums Problem

# Leetcode Lesson: Two Sum

## 1. Problem Statement

Given an array of integers `nums` and an integer `target`, return indices of the two numbers in the array such that they add up to the `target`. You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

**Example 1:**
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

**Example 2:**
Input: nums = [3,2,4], target = 6
Output: [1,2]

**Example 3:**
Input: nums = [3,3], target = 6
Output: [0,1]

**Constraints:**
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.

## 2. Conceptual Understanding

The Two Sum problem asks us to find two numbers in an array that add up to a specific target sum. It's like a puzzle where you're given a bunch of puzzle pieces (the numbers in the array) and you need to find the two pieces that fit together to form a specific picture (the target sum).

In real-world terms, you can think of it as finding two items in a store that add up to a specific amount of money you have to spend.

## 3. Approach Brainstorming

Let's consider a few approaches:

1. **Brute Force**: Check every pair of numbers.
2. **Sorting and Two Pointers**: Sort the array and use two pointers to find the pair.
3. **Hash Map**: Use a hash map to store complements and find the pair in one pass.

Each approach has its own trade-offs in terms of time and space complexity.

## 4. Optimal Solution Walkthrough

The most efficient solution uses a hash map:

1. Create an empty hash map to store numbers and their indices.
2. Iterate through the array.
3. For each number:
   - Calculate its complement (target - current number).
   - If the complement is in the hash map, we've found our pair.
   - If not, add the current number and its index to the hash map.
4. If we finish the loop without finding a pair, return an empty list or raise an exception.

This approach is optimal because it allows us to find the pair in a single pass through the array.

## 5. Python Implementation

```python
def twoSum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []  # No solution found
```

- We use a dictionary `num_map` to store numbers (as keys) and their indices (as values).
- `enumerate(nums)` gives us both the index and value of each element.
- We check if the complement exists in our map before adding the current number.

## 6. Time and Space Complexity Analysis

**Time Complexity**: O(n)
- We iterate through the array once, and each dictionary operation (checking and adding) is O(1) on average.

**Space Complexity**: O(n)
- In the worst case, we might need to store n-1 elements in our dictionary before finding the pair.

This solution optimizes for time complexity at the cost of some additional space.

## 7. Edge Cases and Testing

Consider these test cases:
- `[2,7,11,15], target = 9` (solution at the beginning)
- `[3,2,4], target = 6` (solution in the middle)
- `[3,3], target = 6` (duplicate numbers)
- `[1,5,8,13], target = 14` (solution at the end)
- `[1,2,3,4], target = 10` (no solution)

## 8. Common Pitfalls and Mistakes

- Forgetting to check if the complement exists before adding the current number to the map.
- Returning the numbers instead of their indices.
- Not handling the case where no solution exists.
- Using the same element twice (which is not allowed in this problem).

## 9. Optimization Opportunities

Our solution is already quite optimal, but here are some situational optimizations:
- If the array is very small, a brute force approach might be faster due to less overhead.
- If we know the array is sorted, we could use a two-pointer approach to solve in O(n) time and O(1) space.

## 10. Related Problems and Concepts

- "Three Sum" problem (finding three numbers that add up to a target)
- "Two Sum II - Input Array Is Sorted" (using two pointers)
- Hash tables and dictionaries in general

## 11. Reflection Questions

1. How would the solution change if we needed to return all possible pairs that sum to the target?
2. Can you think of a real-world scenario where finding two numbers that sum to a target is useful?
3. How would you modify this solution to work with a list of strings and concatenation instead of numbers and addition?

## 12. Additional Resources

- [Python Dictionary Operations](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [Time Complexity of Python Operations](https://wiki.python.org/moin/TimeComplexity)
- [Hash Table Data Structure](https://en.wikipedia.org/wiki/Hash_table)
- [Two Pointers Technique](https://leetcode.com/articles/two-pointer-technique/)
