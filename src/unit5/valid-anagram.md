# Valid Anagram Problem

# Leetcode Lesson: Valid Anagram

## 1. Problem Statement

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

**Example 1:**
Input: s = "anagram", t = "nagaram"
Output: true

**Example 2:**
Input: s = "rat", t = "car"
Output: false

**Constraints:**
- 1 <= s.length, t.length <= 5 * 10^4
- s and t consist of lowercase English letters.

## 2. Conceptual Understanding

An anagram is essentially a word or phrase that uses the exact same letters as another word or phrase, just in a different order. Think of it like having two sets of Scrabble tiles - if you can make both words using the same set of tiles (using each tile exactly once), then they're anagrams.

In this problem, we need to determine if two given strings are anagrams of each other. This means checking if they have the same letters in the same quantities, regardless of order.

## 3. Approach Brainstorming

Let's consider a few approaches:
1. **Sorting**: Sort both strings and compare them.
2. **Character Counting**: Count the occurrences of each character in both strings and compare the counts.
3. **Hash Table**: Use a hash table to keep track of character counts.

Each approach has its own trade-offs in terms of time and space complexity.

## 4. Optimal Solution Walkthrough

We'll use the character counting approach, which is efficient and straightforward:

1. First, check if the lengths of the two strings are equal. If not, they can't be anagrams.
2. Create a list of 26 zeros to represent counts of each letter (a-z).
3. Iterate through both strings simultaneously:
   - For each character in s, increment the corresponding count.
   - For each character in t, decrement the corresponding count.
4. If all counts are zero at the end, the strings are anagrams.

This approach is optimal because it only requires a single pass through both strings.

## 5. Python Implementation

```python
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    char_counts = [0] * 26
    
    for c1, c2 in zip(s, t):
        char_counts[ord(c1) - ord('a')] += 1
        char_counts[ord(c2) - ord('a')] -= 1
    
    return all(count == 0 for count in char_counts)
```

- We use a list `char_counts` to keep track of character frequencies.
- `ord(c) - ord('a')` converts a character to an index (0-25).
- `zip(s, t)` allows us to iterate through both strings simultaneously.
- `all()` checks if all counts are zero at the end.

## 6. Time and Space Complexity Analysis

**Time Complexity**: O(n)
- We iterate through both strings once, where n is the length of the strings.
- The final check with `all()` is also O(n), but since it's always 26 operations regardless of input size, it can be considered O(1).

**Space Complexity**: O(1)
- We use a fixed-size list of 26 elements, regardless of input size.

This solution optimizes for both time and space complexity.

## 7. Edge Cases and Testing

Consider these test cases:
- `"anagram"`, `"nagaram"` (valid anagram)
- `"rat"`, `"car"` (not an anagram)
- `"a"`, `"a"` (single character, valid anagram)
- `""`, `""` (empty strings)
- `"aaaaaa"`, `"aaaaaa"` (repeated characters)
- `"ab"`, `"a"` (different lengths)

## 8. Common Pitfalls and Mistakes

- Forgetting to check if the strings have the same length initially.
- Using a dictionary instead of a list for counting, which is less efficient for this specific problem (since we know we only have lowercase letters).
- Sorting the strings, which is less efficient (O(n log n)) than counting.

## 9. Optimization Opportunities

Our solution is already quite optimal, but here are some situational optimizations:
- If the strings are very long, we could stop early if any count exceeds the length of the strings.
- For very short strings, a simple sorting approach might be faster due to less overhead.

## 10. Related Problems and Concepts

- "Group Anagrams" (a more complex version of this problem)
- "Valid Palindrome" (another problem involving character manipulation)
- Hash tables and character encoding

## 11. Reflection Questions

1. How would you modify this solution to handle uppercase letters as well?
2. Can you think of a way to solve this problem using only a single integer variable instead of a list?
3. How would you adapt this solution if you needed to check if one string is a permutation of a substring of another string?

## 12. Additional Resources

- [ASCII Table](https://www.asciitable.com/) (useful for understanding character-to-integer conversion)
- [Python's built-in `ord()` function](https://docs.python.org/3/library/functions.html#ord)
- [Python's `collections.Counter` class](https://docs.python.org/3/library/collections.html#collections.Counter) (an alternative approach using Python's standard library)
