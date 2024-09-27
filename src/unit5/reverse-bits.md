# Reverse bits problem

# Leetcode Lesson: Reverse Bits

## 1. Problem Statement

Reverse bits of a given 32 bits unsigned integer.

**Example 1:**
Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.

**Example 2:**
Input: n = 11111111111111111111111111111101
Output:   3221225471 (10111111111111111111111111111111)
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.

**Constraints:**
- The input must be a binary string of length 32

**Note:**
- Note that in some languages, such as Java, there is no unsigned integer type. In this case, both input and output will be given as a signed integer type. They should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
- In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above, the input represents the signed integer -3 and the output represents the signed integer -1073741825.

## 2. Conceptual Understanding

This problem asks us to reverse the binary representation of a 32-bit unsigned integer. Think of it like reading a 32-character string from right to left instead of left to right.

In binary, each digit represents a power of 2. When we reverse the bits, we're essentially changing which powers of 2 are "turned on" in the number.

For example, if we have:
```
Original: 00000010100101000001111010011100
Reversed: 00111001011110000010100101000000
```
The rightmost '1' bit in the original number becomes the leftmost '1' bit in the reversed number, and so on.

## 3. Approach Brainstorming

Let's consider a few approaches:

1. **String Manipulation**: Convert to binary string, reverse it, convert back to integer.
2. **Bit Manipulation**: Use bitwise operations to reverse the bits in-place.
3. **Lookup Table**: Precompute reversed bytes and use them to build the result.

Each approach has trade-offs in terms of time, space, and ease of understanding.

## 4. Optimal Solution Walkthrough

We'll use the Bit Manipulation approach as it's efficient and doesn't require extra space:

1. Initialize the result as 0.
2. Iterate 32 times (for each bit):
   a. Left-shift the result by 1 to make room for the new bit.
   b. If the rightmost bit of n is 1, add 1 to the result.
   c. Right-shift n by 1 to move to the next bit.
3. Return the result.

This approach directly works with the bits, reversing them one by one.

## 5. Python Implementation

```python
def reverseBits(n):
    result = 0
    for i in range(32):
        result = (result << 1) | (n & 1)
        n >>= 1
    return result
```

- `result << 1` left-shifts the result, making room for the new bit.
- `n & 1` extracts the rightmost bit of n.
- `|` combines the shifted result with the extracted bit.
- `n >>= 1` right-shifts n, moving to the next bit.

## 6. Time and Space Complexity Analysis

**Time Complexity**: O(1)
- We always perform exactly 32 iterations, regardless of the input.

**Space Complexity**: O(1)
- We only use a fixed amount of extra space (the `result` variable).

This solution is optimal in both time and space complexity for this problem.

## 7. Edge Cases and Testing

Consider these test cases:
- `0` (all bits are 0)
- `4294967295` (all bits are 1)
- `43261596` (given in the problem statement)
- `1` (only the rightmost bit is 1)
- `2147483648` (only the leftmost bit is 1)

## 8. Common Pitfalls and Mistakes

- Forgetting that Python integers are not fixed-width, so you need to mask the result to 32 bits if required.
- Misunderstanding the difference between logical and arithmetic right shifts.
- Trying to use string manipulation, which is less efficient and may not work for very large numbers.

## 9. Optimization Opportunities

Our solution is already quite optimal, but here are some situational optimizations:
- For repeated calls, we could use a lookup table for byte reversal to speed up the process.
- In some languages, using unsigned integers can simplify the implementation.

## 10. Related Problems and Concepts

- "Number of 1 Bits" (counting set bits)
- "Single Number" (using XOR operation)
- Bitwise operations in general

## 11. Reflection Questions

1. How would this solution change if we were working with 64-bit integers?
2. Can you think of a real-world application where reversing bits might be useful?
3. How would you modify this function to reverse only the last 16 bits of the number?

## 12. Additional Resources

- [Python Bitwise Operators](https://wiki.python.org/moin/BitwiseOperators)
- [Binary Number System](https://en.wikipedia.org/wiki/Binary_number)
- [Bit Manipulation Techniques](https://www.geeksforgeeks.org/bit-tricks-competitive-programming/)
