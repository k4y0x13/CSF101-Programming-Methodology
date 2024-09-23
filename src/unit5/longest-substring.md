# Longest Substring Without Repeating Characters Problem

# Leetcode Lesson: Longest Substring Without Repeating Characters

## 1. Problem Statement

Given a string `s`, find the length of the longest substring without repeating characters.

**Example 1:**
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

**Example 2:**
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

**Example 3:**
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

**Constraints:**
- 0 <= s.length <= 5 * 10^4
- s consists of English letters, digits, symbols and spaces.

## 2. Conceptual Understanding

This problem asks us to find the longest contiguous sequence of unique characters within a string. We need to keep track of characters we've seen and their positions, updating our "window" of unique characters as we go.

Think of it like a telescope sliding along the string, expanding when it sees new characters and contracting when it encounters repeats.

## 3. Approach Brainstorming

Let's consider a few approaches:
1. **Brute Force**: Check every possible substring for uniqueness.
2. **Sliding Window**: Use two pointers to maintain a window of unique characters.
3. **Sliding Window with Optimization**: Use a dictionary to store character positions for quick lookups.

The sliding window approach is most efficient, as it allows us to solve the problem in a single pass through the string.

## 4. Optimal Solution Walkthrough

We'll use the optimized sliding window approach:

1. Initialize a dictionary to store characters and their indices.
2. Use two pointers, `start` and `end`, to define our window.
3. Iterate through the string with `end`:
   - If the current character is in the dictionary and its index is >= `start`:
     - Update `start` to be one more than the last occurrence of this character.
   - Update the character's position in the dictionary.
   - Update the maximum length if the current window is longer.
4. Return the maximum length found.

This approach allows us to efficiently handle both expanding and contracting our window of unique characters.

## 5. Python Implementation

```python
def lengthOfLongestSubstring(s):
    char_index = {}
    max_length = 0
    start = 0
    
    for end, char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        else:
            max_length = max(max_length, end - start + 1)
        
        char_index[char] = end
    
    return max_length
```

- We use a dictionary `char_index` to store the most recent index of each character.
- `start` and `end` define our current window of unique characters.
- We update `start` when we encounter a repeat character within our current window.
- We update `max_length` whenever we find a longer unique substring.

## 6. Time and Space Complexity Analysis

**Time Complexity**: O(n)
- We iterate through the string once, and dictionary operations are O(1) on average.

**Space Complexity**: O(min(m, n))
- Where m is the size of the character set and n is the length of the string.
- In the worst case, we might store all unique characters in our dictionary.

This solution optimizes for time complexity while using a reasonable amount of extra space.

## 7. Edge Cases and Testing

Consider these test cases:
- `"abcabcbb"` (normal case)
- `"bbbbb"` (all characters the same)
- `"pwwkew"` (longest substring in the middle)
- `""` (empty string)
- `"dvdf"` (tricky case where we need to update start correctly)

## 8. Common Pitfalls and Mistakes

- Forgetting to update the character's position in the dictionary each time.
- Incorrectly updating the `start` pointer (should be one more than the last occurrence).
- Not handling the case where a character repeats but is outside the current window.

## 9. Optimization Opportunities

Our solution is already quite optimal, but here are some situational optimizations:
- If we know the character set is small (e.g., only lowercase letters), we could use a fixed-size array instead of a dictionary.
- We could return early if we reach the maximum possible length (e.g., 26 for lowercase letters).

## 10. Related Problems and Concepts

- "Minimum Window Substring" (more complex sliding window problem)
- "Substring with Concatenation of All Words" (uses similar techniques)
- Hash tables and sliding window technique in general

## 11. Reflection Questions

1. How would this solution change if we needed to return the actual substring instead of just its length?
2. Can you think of a real-world scenario where finding unique sequences is important?
3. How would you modify this solution to find the longest substring with at most two distinct characters?

## 12. Additional Resources

- [Python String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [Sliding Window Technique](https://www.geeksforgeeks.org/window-sliding-technique/)
- [Hash Table Data Structure](https://en.wikipedia.org/wiki/Hash_table)
