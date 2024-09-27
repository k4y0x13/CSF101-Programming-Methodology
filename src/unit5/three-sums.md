# Three Sums Problem

# Leetcode Lesson: Three Sum

## 1. Problem Statement

Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

**Example 1:**
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

**Example 2:**
Input: nums = []
Output: []

**Example 3:**
Input: nums = [0]
Output: []

**Constraints:**
- 0 <= nums.length <= 3000
- -10^5 <= nums[i] <= 10^5

## 2. Conceptual Understanding

This problem asks us to find all unique triplets in the array that sum to zero. It's an extension of the "Two Sum" problem, but with an additional layer of complexity:

1. We need to find three numbers instead of two.
2. We need to find all such triplets, not just one.
3. We need to avoid duplicate triplets in our result.

Think of it as finding all possible combinations of three ingredients that balance each other out to zero on a scale.

## 3. Approach Brainstorming

Let's consider a few approaches:

1. **Brute Force**: Check every possible triplet (O(n^3) time complexity).
2. **Hash Set**: Use a hash set to solve it similar to "Two Sum" for each element (O(n^2) time complexity).
3. **Sorting and Two Pointers**: Sort the array and use two pointers to find complements (O(n^2) time complexity, but more space-efficient).

The sorting approach is generally considered the most efficient for this problem.

## 4. Optimal Solution Walkthrough

We'll use the sorting and two pointers approach:

1. Sort the input array.
2. Iterate through the array with index i.
3. For each i, set two pointers: left (i+1) and right (end of array).
4. While left < right:
   - Calculate the sum of nums[i] + nums[left] + nums[right].
   - If sum == 0, we've found a triplet. Add it to results.
   - If sum < 0, increment left pointer.
   - If sum > 0, decrement right pointer.
5. Skip duplicate values for i to avoid duplicate triplets.

This approach allows us to efficiently find all triplets while avoiding duplicates.

## 5. Python Implementation

```python
def threeSum(nums):
    results = []
    nums.sort()
    
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue  # Skip duplicate values for i
        
        left, right = i + 1, len(nums) - 1
        
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            if total == 0:
                results.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates for left and right
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    
    return results
```

Key points:
- We sort the array first to enable the two-pointer technique.
- We use `continue` to skip duplicate values for `i`.
- We skip duplicate values for `left` and `right` after finding a valid triplet.

## 6. Time and Space Complexity Analysis

**Time Complexity**: O(n^2)
- Sorting takes O(n log n)
- The nested loops (for i and while left < right) take O(n^2)
- Overall, O(n log n + n^2) simplifies to O(n^2)

**Space Complexity**: O(1) or O(n)
- O(1) if we don't count the space for the output
- O(n) if we include the space for the output (in the worst case, we might have O(n) triplets)

The sorting operation typically uses O(log n) extra space.

## 7. Edge Cases and Testing

Consider these test cases:
- `[]` (empty array)
- `[0]` (single element)
- `[0, 0, 0]` (all zeros)
- `[-1, 0, 1]` (single solution)
- `[-4, -1, -1, 0, 1, 2]` (multiple solutions with duplicates)

## 8. Common Pitfalls and Mistakes

- Forgetting to sort the array initially.
- Not handling duplicate values correctly, resulting in duplicate triplets.
- Incorrect bounds in the for loop (should be `range(len(nums) - 2)`).
- Off-by-one errors in the two-pointer logic.

## 9. Optimization Opportunities

- We can potentially exit early if nums[i] > 0, as all subsequent numbers will be positive.
- If the array is very large, we could consider parallelizing the outer loop.

## 10. Related Problems and Concepts

- Two Sum problem
- Four Sum problem
- Two pointers technique
- Sorting algorithms

## 11. Reflection Questions

1. How would this solution change if we were looking for triplets that sum to a target value other than zero?
2. Can you think of a way to solve this problem without sorting the array? What would be the trade-offs?
3. How would you modify this solution to find all quadruplets (4 numbers) that sum to zero?

## 12. Additional Resources

- [Two Pointers Technique](https://www.geeksforgeeks.org/two-pointers-technique/)
- [Python Sorting HOW TO](https://docs.python.org/3/howto/sorting.html)
- [Time Complexity Analysis](https://www.geeksforgeeks.org/understanding-time-complexity-simple-examples/)
