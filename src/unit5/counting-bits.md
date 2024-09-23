# Counting bits problem

# Leetcode Lesson: Counting Bits

## 1. Problem Statement

Given an integer `n`, return an array `ans` of length `n + 1` such that for each `i` (0 <= i <= n), `ans[i]` is the number of 1's in the binary representation of `i`.

**Example 1:**
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

**Example 2:**
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101

**Constraints:**
- 0 <= n <= 10^5

**Follow up:**
- It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
- Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?

## 2. Conceptual Understanding

This problem asks us to count the number of 1's in the binary representation of each number from 0 to n. It's a combination of bit manipulation and dynamic programming concepts.

Think of it as creating a lookup table for the "bit weight" (number of 1's) of each number up to n. This can be useful in various applications, such as error checking in data transmission or certain optimization problems.

## 3. Approach Brainstorming

Let's consider a few approaches:
1. **Brute Force**: Convert each number to binary and count 1's.
2. **Built-in Function**: Use Python's `bin()` and `count()` (not allowed in follow-up).
3. **Bit Manipulation**: Use bitwise operations to count 1's.
4. **Dynamic Programming**: Use previously calculated results to compute new ones.

Each approach has trade-offs in terms of time complexity, space complexity, and adherence to the follow-up constraints.

## 4. Optimal Solution Walkthrough

We'll use a dynamic programming approach that satisfies all constraints:

1. Initialize an array `ans` of size n+1 with all zeros.
2. Set `ans[0] = 0` as our base case.
3. For i from 1 to n:
   - If i is even, the number of 1's is the same as i//2 (right shift by 1).
   - If i is odd, the number of 1's is one more than i-1.

This approach works because:
- For even numbers, the binary representation is the same as the number divided by 2, just with a 0 appended at the end.
- For odd numbers, the binary representation is the same as the previous even number, but with the last bit flipped to 1.

## 5. Python Implementation

```python
def countBits(n):
    ans = [0] * (n + 1)
    for i in range(1, n + 1):
        ans[i] = ans[i >> 1] + (i & 1)
    return ans
```

- We use `i >> 1` to perform an integer division by 2 (right shift by 1 bit).
- `i & 1` checks if the number is odd (1) or even (0).
- This solution avoids using any built-in functions for bit counting.

## 6. Time and Space Complexity Analysis

**Time Complexity**: O(n)
- We iterate through the numbers from 0 to n once.
- Each operation inside the loop (bitwise operations and array access) is O(1).

**Space Complexity**: O(n)
- We create an array of size n+1 to store the results.

This solution meets the follow-up challenge of linear time complexity.

## 7. Edge Cases and Testing

Consider these test cases:
- `n = 0` (edge case: smallest input)
- `n = 1` (to check handling of the first odd number)
- `n = 16` (to check handling of powers of 2)
- `n = 100` (a larger input to verify scaling)

## 8. Common Pitfalls and Mistakes

- Forgetting to handle the base case (n = 0).
- Using built-in functions like `bin()` or `count()`, which don't meet the follow-up requirements.
- Implementing a solution with O(n log n) time complexity (e.g., converting each number to binary).

## 9. Optimization Opportunities

Our solution is already optimal in terms of time and space complexity. However, we could potentially:
- Use bitwise operations more extensively to avoid the modulo operation.
- Implement a cache-friendly version if working with very large n.

## 10. Related Problems and Concepts

- "Number of 1 Bits" (direct application of bit counting)
- "Power of Two" (related to understanding binary representations)
- Dynamic Programming (the technique used in our solution)
- Bit manipulation problems in general

## 11. Reflection Questions

1. How would you modify this solution to count the number of 0's instead of 1's?
2. Can you think of a real-world application where counting bits might be useful?
3. How would you extend this solution to work with negative numbers in two's complement representation?

## 12. Additional Resources

- [Bit Manipulation Tricks](https://graphics.stanford.edu/~seander/bithacks.html)
- [Dynamic Programming on Bit Manipulation](https://www.geeksforgeeks.org/dynamic-programming-on-bit-manipulation/)
- [Python Bitwise Operators](https://wiki.python.org/moin/BitwiseOperators)
