# Exercise

## Example 1
```python
def find_element(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        if arr[i] > target:
            break
    return -1
```
<details>
<summary>Click to see the answer</summary>

Time Complexity: O(n)
Space Complexity: O(1)

Explanation: In the worst case, the function might traverse the entire array (O(n) time). However, it uses only a constant amount of extra space.
</details>

## Example 2
```python
def matrix_search(matrix, target):
    for row in matrix:
        for element in row:
            if element == target:
                return True
            if element > target:
                break
    return False
```
<details>
<summary>Click to see the answer</summary>

Time Complexity: O(m * n)
Space Complexity: O(1)

Explanation: In the worst case, it might search through all elements in the matrix. The space used is constant.
</details>

## Example 3
```python
def find_duplicate(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return num
        seen.add(num)
    return -1
```
<details>
<summary>Click to see the answer</summary>

Time Complexity: O(n)
Space Complexity: O(n)

Explanation: It traverses the array once, but uses a set that could potentially store all elements.
</details>

## Example 4
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```
<details>
<summary>Click to see the answer</summary>

Time Complexity: O(log n)
Space Complexity: O(1)

Explanation: Binary search halves the search space in each iteration. It uses constant extra space.
</details>

## Example 5
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
```
<details>
<summary>Click to see the answer</summary>

Time Complexity: O(n^2)
Space Complexity: O(1)

Explanation: Bubble sort has nested loops, but it can break early if the array is already sorted. Space complexity is constant as it sorts in-place.
</details>

## Example 6
```python
def first_unique_char(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    for i, char in enumerate(s):
        if char_count[char] == 1:
            return i
    return -1
```
<details>
<summary>Click to see the answer</summary>

Time Complexity: O(n)
Space Complexity: O(k), where k is the size of the character set

Explanation: It traverses the string twice. The space used depends on the number of unique characters.
</details>

## Example 7
```python
def max_subarray_sum(arr):
    max_sum = float('-inf')
    current_sum = 0
    for num in arr:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum
```
<details>
<summary>Click to see the answer</summary>

Time Complexity: O(n)
Space Complexity: O(1)

Explanation: It traverses the array once and uses constant extra space.
</details>

## Example 8
```python
def two_sum(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i
    return []
```
<details>
<summary>Click to see the answer</summary>

Time Complexity: O(n)
Space Complexity: O(n)

Explanation: It traverses the array once, but potentially stores all elements in the dictionary.
</details>

## Example 9
```python
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
```
<details>
<summary>Click to see the answer</summary>

Time Complexity: O(n)
Space Complexity: O(1)

Explanation: It potentially checks half of the string characters. It uses constant extra space.
</details>

## Example 10
```python
def find_peak_element(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return left
```
<details>
<summary>Click to see the answer</summary>

Time Complexity: O(log n)
Space Complexity: O(1)

Explanation: It uses binary search to find the peak element. The space used is constant.
</details>

## Example 11
```python
def merge_sorted_arrays(arr1, arr2):
    result = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    return result
```
<details>
<summary>Click to see the answer</summary>

Time Complexity: O(n + m)
Space Complexity: O(n + m)

Explanation: It traverses both arrays once. The space used is proportional to the sum of the lengths of both arrays.
</details>

## Example 12
```python
def count_elements(arr):
    count_dict = {}
    for num in arr:
        if num in count_dict:
            break
        count_dict[num] = count_dict.get(num, 0) + 1
    return len(count_dict)
```
<details>
<summary>Click to see the answer</summary>

Time Complexity: O(n)
Space Complexity: O(n)

Explanation: It may traverse the entire array, but breaks on the first duplicate. The space used could be up to the size of the array if all elements are unique.
</details>

## Example 13
```python
def first_bad_version(n):
    left, right = 1, n
    while left < right:
        mid = left + (right - left) // 2
        if is_bad_version(mid):
            right = mid
        else:
            left = mid + 1
    return left

def is_bad_version(version):
    # This is a mock function
    pass
```
<details>
<summary>Click to see the answer</summary>

Time Complexity: O(log n)
Space Complexity: O(1)

Explanation: It uses binary search to find the first bad version. The space used is constant.
</details>

## Example 14
```python
def longest_common_prefix(strs):
    if not strs:
        return ""
    for i in range(len(strs[0])):
        for string in strs[1:]:
            if i >= len(string) or string[i] != strs[0][i]:
                return strs[0][:i]
    return strs[0]
```
<details>
<summary>Click to see the answer</summary>

Time Complexity: O(S), where S is the sum of all characters in all strings
Space Complexity: O(1)

Explanation: It compares characters from all strings. The space used is constant as it only returns a slice of the first string.
</details>

## Example 15
```python
def find_single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result
```
<details>
<summary>Click to see the answer</summary>

Time Complexity: O(n)
Space Complexity: O(1)

Explanation: It traverses the array once, using the XOR operation. The space used is constant.
</details>

## Example 16

```python
def count_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1
    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])
    return sorted_arr
```
<details>
<summary>Click to see the answer</summary>

Time Complexity: O(n + k), where k is the range of input
Space Complexity: O(k)

Explanation: It makes two passes through the input and one pass through the count array. The space used depends on the range of input values.
</details>

## Example 17
```python
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]
```
<details>
<summary>Click to see the answer</summary>

Time Complexity: O(n)
Space Complexity: O(n)

Explanation: With memoization, each Fibonacci number is calculated only once. The space used is proportional to n for the memoization dictionary and the call stack.
</details>

## Example 18
```python
def quick_select(arr, k):
    def partition(left, right, pivot_idx):
        pivot = arr[pivot_idx]
        arr[pivot_idx], arr[right] = arr[right], arr[pivot_idx]
        store_idx = left
        for i in range(left, right):
            if arr[i] < pivot:
                arr[store_idx], arr[i] = arr[i], arr[store_idx]
                store_idx += 1
        arr[right], arr[store_idx] = arr[store_idx], arr[right]
        return store_idx

    def select(left, right):
        if left == right:
            return arr[left]
        pivot_idx = (left + right) // 2
        pivot_idx = partition(left, right, pivot_idx)
        if k == pivot_idx:
            return arr[k]
        elif k < pivot_idx:
            return select(left, pivot_idx - 1)
        else:
            return select(pivot_idx + 1, right)

    return select(0, len(arr) - 1)
```
<details>
<summary>Click to see the answer</summary>

Time Complexity: O(n) average case, O(n^2) worst case
Space Complexity: O(log n) average case due to recursion

Explanation: Quick select is similar to quicksort but only recurses on one side. On average, it eliminates half the elements in each recursion.
</details>

## Example 19
```python
def rabin_karp(text, pattern):
    if not pattern:
        return 0
    p, t = 0, 0
    p_len, t_len = len(pattern), len(text)
    for i in range(p_len):
        p = (p * 256 + ord(pattern[i])) % 101
        t = (t * 256 + ord(text[i])) % 101
    for i in range(t_len - p_len + 1):
        if p == t:
            if text[i:i+p_len] == pattern:
                return i
        if i < t_len - p_len:
            t = (t - ord(text[i]) * pow(256, p_len-1, 101)) % 101
            t = (t * 256 + ord(text[i+p_len])) % 101
            t = (t + 101) % 101
    return -1
```
<details>
<summary>Click to see the answer</summary>

Time Complexity: O(n+m) average case, O(nm) worst case
Space Complexity: O(1)

Explanation: Rabin-Karp algorithm for pattern matching. It uses rolling hash to compare substrings efficiently. Worst case occurs when all hash values match but strings don't.
</details>

## Example 20
```python
def longest_increasing_subsequence(nums):
    if not nums:
        return 0
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
```
<details>
<summary>Click to see the answer</summary>

Time Complexity: O(n^2)
Space Complexity: O(n)

Explanation: It uses dynamic programming to compute the length of the longest increasing subsequence. The space used is proportional to the input size.
</details>

## Example 21
```python
def is_power_of_two(n):
    if n <= 0:
        return False
    return n & (n - 1) == 0
```
<details>
<summary>Click to see the answer</summary>

Time Complexity: O(1)
Space Complexity: O(1)

Explanation: It uses a bitwise operation to check if a number is a power of two. Both time and space complexity are constant.
</details>

## Example 22
```python
def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return [i for i in range(2, n + 1) if primes[i]]
```
<details>
<summary>Click to see the answer</summary>

Time Complexity: O(n log log n)
Space Complexity: O(n)

Explanation: The Sieve of Eratosthenes efficiently finds all primes up to n. The space used is proportional to n for the boolean array.
</details>

## Example 23
```python
def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]], dp[i-1][w])
            else
                dp[i][w] = dp[i-1][w]
    return dp[n][capacity]
```
<details>
<summary>Click to see the answer</summary>

Time Complexity: O(n * capacity)
Space Complexity: O(n * capacity)

Explanation: This is the dynamic programming solution to the 0/1 Knapsack problem. Both time and space complexity are proportional to the number of items and the knapsack capacity.
</details>

## Example 24
```python
def find_missing_number(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum
```
<details>
<summary>Click to see the answer</summary>

Time Complexity: O(n)
Space Complexity: O(1)

Explanation: It calculates the expected sum of numbers from 0 to n and subtracts the actual sum of the array. It uses constant extra space.
</details>

## Example 25
```python
def boyer_moore_majority(nums):
    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    return candidate
```
<details>
<summary>Click to see the answer</summary>

Time Complexity: O(n)
Space Complexity: O(1)

Explanation: Boyer-Moore majority vote algorithm finds a majority element (if it exists) in linear time with constant extra space.
</details>

## Example 26
```python
def jump_game(nums):
    max_reach = 0
    for i in range(len(nums)):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + nums[i])
    return True
```
<details>
<summary>Click to see the answer</summary>

Time Complexity: O(n)
Space Complexity: O(1)

Explanation: It keeps track of the maximum reachable index. It traverses the array once and uses constant extra space.
</details>

## Example 27
```python
def longest_palindrome_subseq(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for cl in range(2, n + 1):
        for i in range(n - cl + 1):
            j = i + cl - 1
            if s[i] == s[j] and cl == 2:
                dp[i][j] = 2
            elif s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    return dp[0][n-1]
```
<details>
<summary>Click to see the answer</summary>

Time Complexity: O(n^2)
Space Complexity: O(n^2)

Explanation: Dynamic programming solution for finding the longest palindromic subsequence. It uses a 2D array to store intermediate results.
</details>

## Example 28
```python
from collections import deque

def sliding_window_maximum(nums, k):
    result = []
    window = deque()
    for i, num in enumerate(nums):
        while window and window[0] <= i - k:
            window.popleft()
        while window and nums[window[-1]] < num:
            window.pop()
        window.append(i)
        if i >= k - 1:
            result.append(nums[window[0]])
    return result
```
<details>
<summary>Click to see the answer</summary>

Time Complexity: O(n)
Space Complexity: O(k)

Explanation: It uses a deque to maintain the maximum element in the current window. Each element is pushed and popped at most once.
</details>

## Example 29
```python
def min_cost_climbing_stairs(cost):
    n = len(cost)
    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
    return dp[n]
```
<details>
<summary>Click to see the answer</summary>

Time Complexity: O(n)
Space Complexity: O(n)

Explanation: Dynamic programming solution for the min cost climbing stairs problem. It uses an array to store the minimum cost to reach each step.
</details>

## Example 30
```python
def next_greater_element(nums):
    n = len(nums)
    result = [-1] * n
    stack = []
    for i in range(2*n-1, -1, -1):
        while stack and stack[-1] <= nums[i%n]:
            stack.pop()
        if stack:
            result[i%n] = stack[-1]
        stack.append(nums[i%n])
    return result
```
<details>
<summary>Click to see the answer</summary>

Time Complexity: O(n)
Space Complexity: O(n)

Explanation: It uses a stack to find the next greater element for each number in the array. It simulates the circular nature of the array by iterating twice.
</details>
