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
https://leetcode.com/problems/contains-duplicate <br>
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example: <br>
Input: nums = [1,2,3,1] <br>
Output: true <br>
Explanation: The element 1 occurs at the indices 0 and 3.

Input: nums = [1,2,3,4] <br>
Output: false <br>
Explanation: All elements are distinct.


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
https://leetcode.com/problems/valid-anagram <br>
Given two strings s and t, return true if t is an anagram of s, and false otherwise. Anagram is a word, phrase, or name formed by rearranging the letters of another.

Example: <br>
Input: s = "anagram", t = "nagaram" <br>
Output: true <br>

Input: s = "rat", t = "car" <br>
Output: false <br>


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
https://leetcode.com/problems/two-sum <br>
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.

Example: <br>
Input: nums = [2,7,11,15], target = 9 <br>
Output: [0,1]  <br>
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]. 

Input: nums = [3,2,4], target = 6  <br>
Output: [1,2] <br>

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

#### Valid Palindrome
https://leetcode.com/problems/valid-palindrome <br>
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers. Given a string s, return true if it is a palindrome, or false otherwise.

Example: <br>
Input: s = "A man, a plan, a canal: Panama" <br>
Output: true <br>
Explanation: "amanaplanacanalpanama" is a palindrome. <br>

Input: s = "race a car" <br>
Output: false <br>
Explanation: "raceacar" is not a palindrome. <br>

Python 3
```Python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [c.lower() for c in s if c.isalnum()]
        return all (s[i] == s[~i] for i in range(len(s)//2))
```

Python
```Python
class Solution:
    def isPalindrome(self, s):
        s = [c.lower() for c in s if c.isalnum()]
        return all (s[i] == s[~i] for i in range(len(s)//2))
```

#### Three Sum
https://leetcode.com/problems/3sum <br>
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0. Notice that the solution set must not contain duplicate triplets.

Example: <br>
Input: nums = [-1,0,1,2,-1,-4] <br>
Output: [[-1,-1,2],[-1,0,1]] <br>
Explanation:  <br>
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0. <br>
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0. <br>
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0. <br>
The distinct triplets are [-1,0,1] and [-1,-1,2]. <br>
Notice that the order of the output and the order of the triplets does not matter. <br>

Input: nums = [0,1,1] <br>
Output: [] <br>
Explanation: The only possible triplet does not sum up to 0.

Python 3
```Python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target = 0
        nums.sort()
        s = set()
        output = []
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == target:
                    s.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif sum < target:
                    j += 1
                else:
                    k -= 1
        output = list(s)
        return output
```

Python
```python
class Solution:
    def threeSum(self, nums):
        target = 0
        nums.sort()
        s = set()
        output = []
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == target:
                    s.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif sum < target:
                    j += 1
                else:
                    k -= 1
        output = list(s)
        return output
```

### Step 3: Algorithm Problems Sliding Window (Best Time to Buy And Sell Stock), Longest Substring Without Repeating Characters
Leetcode problems on Sliding Window (Best Time to Buy And Sell Stock), Longest Substring Without Repeating Characters

#### Best Time to Buy And Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock <br>
You are given an array prices where prices[i] is the price of a given stock on the ith day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example: <br>
Input: prices = [7,1,5,3,6,4] <br>
Output: 5  <br>
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5. Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell. 

Python
```python
class Solution:
    def maxProfit(self, prices):
        buy = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i] - buy > profit:
                profit = prices[i] - buy
        return profit
```
#### Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters <br>
Given a string s, find the length of the longest without duplicate characters.

Example: <br>
Input: s = "abcabcbb” <br>
Output: 3 <br>
Explanation: The answer is "abc", with the length of 3.

Input: s = "bbbbb" <br>
Output: 1  <br>
Explanation: The answer is "b", with the length of 1. 

```python
class Solution:
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        maxLength = 0
        charSet = set()
        left = 0
        for right in range(n):
            if s[right] not in charSet:
                charSet.add(s[right])
                maxLength = max(maxLength, right - left + 1)
            else:
                while s[right] in charSet:
                    charSet.remove(s[left])
                    left += 1
                charSet.add(s[right])
        return maxLength
```

## Exercises for Students

1. 

## Conclusion

In this lab, you've implemented some algorithms: Contains Duplicate, Valid Anagram, Two Sums, Valid Palindrome, Three Sums and Sliding Window Exercises.

Key takeaways:
- How to create algorithms that solve specific problems.

