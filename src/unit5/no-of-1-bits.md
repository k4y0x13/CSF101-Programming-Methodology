# Number of 1 bits problem

# Leetcode Lesson: Number of 1 Bits

## 1. Problem Statement

Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

**Example 1:**
Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

**Example 2:**
Input: n = 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.

**Example 3:**
Input: n = 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.

**Constraints:**
- The input must be a binary string of length 32.

## 2. Conceptual Understanding

This problem is asking us to count the number of 1s in the binary representation of a given integer. In binary, each digit represents a power of 2, and 1s indicate which powers of 2 are included in the number.

Think of it like counting how many lights are on in a row of 32 light switches, where each switch represents a bit.

## 3. Approach Brainstorming

Let's consider a few approaches:
1. **String Conversion**: Convert the number to a binary string and count the 1s.
2. **Bit Shifting**: Repeatedly shift the bits and check the least significant bit.
3. **Brian Kernighan's Algorithm**: Use a clever bit manipulation trick.

Each approach has different implications for time complexity and ease of understanding.

## 4. Optimal Solution Walkthrough

We'll use Brian Kernighan's Algorithm, which is both efficient and interesting:

1. Initialize a count to 0.
2. While the number is not 0:
   - Perform the operation: n = n & (n - 1)
   - Increment the count.
3. Return the count.

This algorithm works because n & (n - 1) always removes the rightmost 1-bit from n. We repeat this until n becomes 0.

## 5. Python Implementation

```python
def hammingWeight(n: int) -> int:
    count = 0
    while n:
        n &= (n - 1)
        count += 1
    return count
```

- We use the bitwise AND operator `&` to perform n & (n - 1).
- The loop continues as long as n is not 0.
- Each iteration removes one 1-bit and increments the count.

## 6. Time and Space Complexity Analysis

**Time Complexity**: O(k), where k is the number of 1-bits in n.
- In the worst case (all bits are 1), this is O(32) for a 32-bit integer, which is effectively O(1).

**Space Complexity**: O(1)
- We only use a single integer variable for counting, regardless of the input size.

This solution is very efficient in both time and space.

## 7. Edge Cases and Testing

Consider these test cases:
- `0` (no 1-bits)
- `1` (single 1-bit)
- `2147483647` (0x7FFFFFFF, all 1s except the sign bit)
- `4294967295` (0xFFFFFFFF, all 1s)
- `2147483648` (0x80000000, only the sign bit is 1)

## 8. Common Pitfalls and Mistakes

- Forgetting that Python integers are not fixed-width, so very large numbers might cause issues.
- Using a loop that always iterates 32 times, which is less efficient.
- Confusing bitwise operators (& vs |, etc.)

## 9. Optimization Opportunities

Our solution is already quite optimal, but here are some alternatives:
- Using a lookup table for small numbers or byte-sized chunks could be faster for some inputs.
- Some processors have a built-in instruction to count 1-bits (popcount), which Python's `bin(n).count('1')` might use internally.

## 10. Related Problems and Concepts

- "Counting Bits" (calculate Hamming weight for a range of numbers)
- "Power of Two" (check if a number has exactly one 1-bit)
- Bitwise operations in general

## 11. Reflection Questions

1. How would you solve this problem if you were limited to using only addition and subtraction?
2. Can you think of a real-world application where counting 1-bits is important?
3. How might this algorithm be useful in data compression or error checking?

## 12. Additional Resources

- [Bitwise Operations in Py
