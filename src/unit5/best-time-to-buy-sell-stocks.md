# Best Time to Buy & Sell Stocks

# Leetcode Lesson: Best Time to Buy and Sell Stock

## 1. Problem Statement

You are given an array `prices` where `prices[i]` is the price of a given stock on the `i`th day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

**Example 1:**
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

**Example 2:**
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

**Constraints:**
- 1 <= prices.length <= 10^5
- 0 <= prices[i] <= 10^4

## 2. Conceptual Understanding

This problem is about finding the maximum difference between two numbers in an array, where the smaller number comes before the larger number.

Think of it as trying to buy a stock at its lowest price and sell it at its highest price, but you can only look at past prices when making a decision to buy.

## 3. Approach Brainstorming

Let's consider a few approaches:
1. **Brute Force**: Check every pair of buy and sell days.
2. **Two Pointers**: Use two pointers to keep track of buy and sell days.
3. **One Pass**: Keep track of the minimum price and maximum profit as we iterate.

Each approach has trade-offs in terms of time and space complexity.

## 4. Optimal Solution Walkthrough

The most efficient solution uses a one-pass approach:

1. Initialize variables for minimum price (set to infinity) and maximum profit (set to 0).
2. Iterate through the prices array.
3. For each price:
   - If it's less than the minimum price, update the minimum price.
   - Calculate the potential profit if we sell at this price.
   - If this potential profit is greater than our maximum profit, update the maximum profit.
4. Return the maximum profit.

This approach is optimal because it solves the problem in a single pass through the array.

## 5. Python Implementation

```python
def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit
```

- We use `float('inf')` to initialize `min_price` to positive infinity.
- We update `min_price` whenever we find a lower price.
- We calculate and update `max_profit` if we find a better selling opportunity.

## 6. Time and Space Complexity Analysis

**Time Complexity**: O(n)
- We iterate through the prices array once, performing constant time operations at each step.

**Space Complexity**: O(1)
- We only use two variables (`min_price` and `max_profit`) regardless of the input size.

This solution optimizes for both time and space complexity.

## 7. Edge Cases and Testing

Consider these test cases:
- `[7,1,5,3,6,4]` (normal case with profit)
- `[7,6,4,3,1]` (decreasing prices, no profit)
- `[1,2]` (minimum length array with profit)
- `[1]` (single element array)
- `[3,3,3,3,3]` (all prices the same)

## 8. Common Pitfalls and Mistakes

- Forgetting to handle the case where no profit is possible (should return 0).
- Trying to keep track of both buy and sell days, which isn't necessary for this problem.
- Using a two-pass solution (one to find minimum, one to find maximum profit) which is less efficient.

## 9. Optimization Opportunities

Our solution is already quite optimal, but here are some situational optimizations:
- If we needed to return the buy and sell days, we could modify the algorithm to keep track of these indices.
- For very large arrays, we could potentially use parallel processing to split the array and find local min/max in each section.

## 10. Related Problems and Concepts

- "Best Time to Buy and Sell Stock II" (allowed to do multiple transactions)
- "Maximum Subarray" (similar concept of keeping track of best so far)
- Dynamic Programming (this problem can be seen as a simple form of DP)

## 11. Reflection Questions

1. How would this algorithm change if you were allowed to buy and sell multiple times?
2. Can you think of a real-world scenario where this type of algorithm might be useful outside of stock trading?
3. How would you modify this solution if you needed to return the buy and sell days instead of the maximum profit?

## 12. Additional Resources

- [Dynamic Programming](https://en.wikipedia.org/wiki/Dynamic_programming)
- [Kadane's Algorithm](https://en.wikipedia.org/wiki/Maximum_subarray_problem) (related problem)
- [Python's built-in functions](https://docs.python.org/3/library/functions.html) (for understanding `float('inf')`)
