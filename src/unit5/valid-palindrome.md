# Valid Palindrome Problem

# Leetcode Lesson: Valid Palindrome

## 1. Problem Statement

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

**Example 1:**
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

**Example 2:**
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

**Example 3:**
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters. Since an empty string reads the same forward and backward, it is a palindrome.

**Constraints:**
- 1 <= s.length <= 2 * 10^5
- s consists only of printable ASCII characters.

## 2. Conceptual Understanding

A palindrome is a sequence that reads the same backwards as forwards. In this problem, we need to:
1. Clean the string by removing non-alphanumeric characters and converting to lowercase.
2. Check if the cleaned string is equal to its reverse.

Think of it like a mirror image of words or phrases.

## 3. Approach Brainstorming

Let's consider a few approaches:
1. **Clean and Reverse**: Clean the string, reverse it, and compare.
2. **Two Pointers**: Use two pointers moving from both ends towards the center.
3. **Stack/Queue**: Use a stack or queue to compare characters.

Each approach has trade-offs in terms of time and space complexity.

## 4. Optimal Solution Walkthrough

We'll use the Two Pointers approach as it's efficient and doesn't require extra space:

1. Initialize two pointers: one at the start and one at the end of the string.
2. Move the pointers towards each other, skipping non-alphanumeric characters.
3. Compare the characters at both pointers.
4. If at any point the characters don't match, it's not a palindrome.
5. If the pointers meet or cross without finding a mismatch, it's a palindrome.

This approach is optimal because it checks the string in a single pass and uses constant extra space.

## 5. Python Implementation

```python
def isPalindrome(s):
    left, right = 0, len(s) - 1
    
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True
```

- We use `isalnum()` to check if a character is alphanumeric.
- `lower()` converts characters to lowercase for comparison.
- The outer while loop continues until the pointers meet or cross.
- The inner while loops skip non-alphanumeric characters.

## 6. Time and Space Complexity Analysis

**Time Complexity**: O(n)
- We traverse the string once, where n is the length of the string.
- Each character is visited at most twice (once by each pointer).

**Space Complexity**: O(1)
- We only use a constant amount of extra space (two pointers).

This solution optimizes both time and space complexity.

## 7. Edge Cases and Testing

Consider these test cases:
- "A man, a plan, a canal: Panama" (valid palindrome with punctuation)
- "race a car" (not a palindrome)
- " " (empty string, considered a palindrome)
- "a" (single character, always a palindrome)
- "Aa" (case insensitive palindrome)
- "0P" (mix of numbers and letters, not a palindrome)

## 8. Common Pitfalls and Mistakes

- Forgetting to handle non-alphanumeric characters.
- Not making the comparison case-insensitive.
- Incorrectly handling empty strings or strings with a single character.
- Using extra space unnecessarily (e.g., creating a new cleaned string).

## 9. Optimization Opportunities

Our two-pointer solution is already quite optimal, but here are some situational optimizations:
- For very long strings, we could potentially use multiple threads to check different parts simultaneously.
- If this function is called frequently, we could implement caching for common inputs.

## 10. Related Problems and Concepts

- "Longest Palindromic Substring"
- "Palindrome Number"
- String manipulation and two-pointer technique in general

## 11. Reflection Questions

1. How would you modify this solution to find the longest palindromic substring?
2. Can you think of a real-world application where checking for palindromes might be useful?
3. How would you solve this problem if you needed to ignore spaces in addition to non-alphanumeric characters?

## 12. Additional Resources

- [Python String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [Two Pointer Technique](https://leetcode.com/articles/two-pointer-technique/)
- [ASCII Table](https://www.asciitable.com/) (for understanding printable ASCII characters)
