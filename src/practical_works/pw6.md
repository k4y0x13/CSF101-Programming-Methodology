# Practical 6: Algorithms Exercises on Arrays, Hashing, Two Pointers, Sliding Window

## Objective
In this lab, you will implement following algorithms: Valid Anagram, Two Sums, Valid Palindrome, Three Sums, Sliding Window Exercises. This exercise will help you understand the mechanics of these algorithms and compare their performance.

**Submission Date:** November 4st

## Prerequisites
- Basic knowledge of Python syntax
- Understanding of lists and functions in Python
- Familiarity with time complexity concepts (optional, but helpful)

## Lab Steps

### Step 1: Algorithm Problems on Contains Duplicate, Valid Anagram, Two Sums
Leetcode problems on Contains Duplicate, Valid Anagram, Two Sums

#### Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example:
Input: nums = [1,2,3,1]
Output: true
Explanation: The element 1 occurs at the indices 0 and 3.

Input: nums = [1,2,3,4]
Output: false
Explanation: All elements are distinct.

https://leetcode.com/problems/contains-duplicate

Python
```python
class Solution:
	def containsDuplicate(self, nums):
		return len(set(nums))!=len(nums)
```

Python 3
```python
class Solution:
	def containsDuplicate(self, nums: List[int]) -> bool:
		return len(set(nums))!=len(nums)
```

#### Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise. Anagram is a word, phrase, or name formed by rearranging the letters of another.<img width="2065" alt="image" src="https://github.com/user-attachments/assets/e995f5ff-8a8c-47e5-8c11-56b87746d614" />

Example:
Input: s = "anagram", t = "nagaram"
Output: true

Input: s = "rat", t = "car"
Output: false

https://leetcode.com/problems/valid-anagram

Python
```python
class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        return (len(set(count)) == 1 and list(set(count))[0] == 0)
```

Python 3
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        return (len(set(count)) == 1 and list(set(count))[0] == 0)
```

#### Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1] 
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]. 

Input: nums = [3,2,4], target = 6 
Output: [1,2]

https://leetcode.com/problems/two-sum

Python3
```Python
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(1, len(nums)):
            for j in range(i, len(nums)):
                if nums[j] + nums[j - i] == target:
                    return [j, j - i]
        return []
```

Python
```Python
class Solution:
    def twoSum(self, nums, target):
        for i in range(1, len(nums)):
            for j in range(i, len(nums)):
                if nums[j] + nums[j - i] == target:
                    return [j, j - i]
        return []
```

### Step 2: Algorithm Problems on Valid Palindrome, Three Sums
Leetcode problems on Valid Palindrome, Three Sums

https://leetcode.com/problems/valid-palindrome

https://leetcode.com/problems/3sum

```python

```

### Step 3: Algorithm Problems Sliding Window (Best Time to Buy And Sell Stock), Longest Substring Without Repeating Characters
Leetcode problems on Sliding Window (Best Time to Buy And Sell Stock), Longest Substring Without Repeating Characters

https://leetcode.com/problems/best-time-to-buy-and-sell-stock

https://leetcode.com/problems/longest-substring-without-repeating-characters

```python

```


## Exercises for Students

1. Implement

## Conclusion

In this lab, you've implemented some algorithms: Contains Duplicate, Valid Anagram, Two Sums, Valid Palindrome, Three Sums and Sliding Window Exercises.

Key takeaways:
- 

