# Climbing Stairs Problem

# Leetcode Lesson: Climbing Stairs

## 1. Problem Statement

You are climbing a staircase. It takes `n` steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

**Example 1:**
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

**Example 2:**
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

**Constraints:**
- 1 <= n <= 45

## 2. Conceptual Understanding

This problem is about finding the number of different combinations to reach a goal (the top of the stairs) given a set of fixed moves (1 or 2 steps at a time).

Think of it like this: You're standing at the bottom of a staircase, and for each step, you have two choices: take 1 step or take 2 steps. We need to count all the possible sequences of these choices that lead to the top.

This problem introduces the concept of dynamic programming, where we build the solution to a larger problem from solutions to smaller subproblems.

## 3. Approach Brainstorming

Let's consider a few approaches:
1. **Recursive**: Solve the problem by breaking it down into smaller subproblems.
2. **Dynamic Programming**: Build up the solution iteratively, storing intermediate results.
3. **Mathematical**: Recognize the pattern and use a formula (this is actually the Fibonacci sequence).

Each approach has trade-offs in terms of time and space complexity, as well as ease of understanding.

## 4. Optimal Solution Walkthrough

We'll use the Dynamic Programming approach:

1. Create an array `dp` where `dp[i]` represents the number of ways to climb to the i-th step.
2. Initialize the base cases: `dp[1] = 1` (one way to climb 1 step) and `dp[2] = 2` (two ways to climb 2 steps).
3. For steps 3 to n, the number of ways to reach step i is the sum of ways to reach the previous step (and then take 1 step) and the ways to reach two steps back (and then take 2 steps).
   So, `dp[i] = dp[i-1] + dp[i-2]`
4. Return `dp[n]` as the final answer.

This approach is optimal because it solves each subproblem only once and uses the results to build up to the final solution.

## 5. Python Implementation

```python
def climbStairs(n):
    if n <= 2:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]
```

- We use a list `dp` to store the number of ways for each step.
- We initialize the base cases for 1 and 2 steps.
- We then iterate from 3 to n, filling in the `dp` array.
- The final answer is in `dp[n]`.

## 6. Time and Space Complexity Analysis

**Time Complexity**: O(n)
- We iterate through the steps once, performing constant-time operations at each step.

**Space Complexity**: O(n)
- We use an array of size n+1 to store intermediate results.

Note: We can optimize the space complexity to O(1) by only keeping track of the last two values instead of the entire array.

## 7. Edge Cases and Testing

Consider these test cases:
- `n = 1` (base case)
- `n = 2` (base case)
- `n = 3` (first non-base case)
- `n = 5` (a medium-sized case)
- `n = 45` (the maximum input according to the constraints)

## 8. Common Pitfalls and Mistakes

- Forgetting to handle the base cases (n = 1 and n = 2) separately.
- Confusing the problem with counting the number of steps, rather than the number of ways to take steps.
- Trying to generate all possible combinations explicitly, which is inefficient for larger n.

## 9. Optimization Opportunities

We can optimize the space complexity:

```python
def climbStairs(n):
    if n <= 2:
        return n
    
    prev, curr = 1, 2
    for _ in range(3, n + 1):
        prev, curr = curr, prev + curr
    
    return curr
```

This solution uses only O(1) extra space.

## 10. Related Problems and Concepts

- Fibonacci Sequence (this problem follows the same pattern)
- "House Robber" problem (another dynamic programming problem)
- Other dynamic programming problems like "Coin Change" or "Minimum Cost Climbing Stairs"

## 11. Reflection Questions

1. How does this problem relate to the Fibonacci sequence?
2. Can you think of a real-world scenario that follows a similar pattern?
3. How would the solution change if you could take 1, 2, or 3 steps at a time?
4. Can you solve this problem recursively? How would the time complexity compare?

## 12. Additional Resources

- [Introduction to Dynamic Programming](https://www.geeksforgeeks.org/dynamic-programming/)
- [Fibonacci Sequence](https://en.wikipedia.org/wiki/Fibonacci_number)
- [Time and Space Complexity Analysis](https://www.geeksforgeeks.org/time-complexity-and-space-complexity/)
