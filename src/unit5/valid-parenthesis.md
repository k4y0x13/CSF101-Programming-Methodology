# Valid Parenthesis Problem

# Leetcode Lesson: Valid Parentheses

## 1. Problem Statement

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

**Example 1:**
Input: s = "()"
Output: true

**Example 2:**
Input: s = "()[]{}"
Output: true

**Example 3:**
Input: s = "(]"
Output: false

**Constraints:**
- 1 <= s.length <= 10^4
- `s` consists of parentheses only `'()[]{}'`

## 2. Conceptual Understanding

This problem is about validating the structure of nested parentheses. It's similar to checking if HTML tags or code blocks are properly nested and closed.

Think of it like nesting dolls: each smaller doll (inner parenthesis) needs to be completely enclosed by its larger doll (outer parenthesis) of the same type.

## 3. Approach Brainstorming

Let's consider a few approaches:
1. **Counting**: Count opening and closing brackets (doesn't work for all cases).
2. **Stack**: Use a stack to keep track of opening brackets.
3. **Replace Pairs**: Repeatedly replace valid pairs with empty string (inefficient for large inputs).

The stack approach is usually the most efficient and intuitive.

## 4. Optimal Solution Walkthrough

We'll use a stack-based approach:

1. Initialize an empty stack.
2. Iterate through each character in the string:
   - If it's an opening bracket, push it onto the stack.
   - If it's a closing bracket:
     - If the stack is empty, return False (no matching opening bracket).
     - If the top of the stack doesn't match the current closing bracket, return False.
     - If it matches, pop the top element from the stack.
3. After the loop, return True if the stack is empty, False otherwise.

This approach ensures that brackets are closed in the correct order and that every closing bracket has a matching opening bracket.

## 5. Python Implementation

```python
def isValid(s: str) -> bool:
    stack = []
    bracket_map = {")": "(", "}": "{", "]": "["}
    
    for char in s:
        if char in bracket_map:  # it's a closing bracket
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()
        else:  # it's an opening bracket
            stack.append(char)
    
    return len(stack) == 0
```

- We use a list `stack` to simulate a stack data structure.
- `bracket_map` is a dictionary that maps closing brackets to their corresponding opening brackets.
- `stack[-1]` accesses the top element of the stack.
- `stack.pop()` removes and returns the top element of the stack.
- `stack.append(char)` adds an element to the top of the stack.

## 6. Time and Space Complexity Analysis

**Time Complexity**: O(n)
- We iterate through the string once, and each stack operation (push, pop, top) is O(1).

**Space Complexity**: O(n)
- In the worst case (e.g., "((((", we might push all characters onto the stack.

## 7. Edge Cases and Testing

Consider these test cases:
- `"()"` (simplest valid case)
- `"()[]{}"` (multiple valid pairs)
- `"(]"` (mismatched brackets)
- `"([)]"` (correct types but wrong order)
- `"{[]}"` (nested brackets)
- `""` (empty string)
- `"((("` (only opening brackets)
- `")))"` (only closing brackets)

## 8. Common Pitfalls and Mistakes

- Forgetting to check if the stack is empty before accessing its top element.
- Not handling the case where there are leftover opening brackets.
- Confusing the order of checking (always check closing brackets against the last opening bracket).

## 9. Optimization Opportunities

Our solution is already quite optimal, but here are some minor optimizations:
- We could return False early if the string length is odd.
- For very long strings, we could use a deque instead of a list for slightly better performance.

## 10. Related Problems and Concepts

- "Generate Parentheses" (generating all combinations of valid parentheses)
- "Longest Valid Parentheses" (finding the longest valid substring)
- Stack-based problems in general
- Parsing and syntax validation in compilers

## 11. Reflection Questions

1. How would you modify this solution to also return the position of the first invalid character?
2. Can you think of a real-world scenario where validating nested structures is important?
3. How would you extend this solution to handle more types of brackets or even HTML tags?

## 12. Additional Resources

- [Python List as Stack](https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-stacks)
- [Stack Data Structure](https://en.wikipedia.org/wiki/Stack_(abstract_data_type))
- [Balanced Brackets Problem](https://www.hackerrank.com/challenges/balanced-brackets/problem)
