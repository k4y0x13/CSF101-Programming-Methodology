# Quiz Time-Space Exercise

# Time and Space Complexity Practice Questions for Beginner Python Programmers

This document contains 33 practice questions to help you understand time and space complexity in Python. For each question, you'll see a Python code snippet. Try to determine the time and space complexity before revealing the answer and explanation.

## Question 1

What is the time and space complexity of the given code below:

```python
def sum_numbers(n):
    total = 0
    for i in range(n):
        total += i
    return total
```

<details>
<summary>Answer</summary>
Time Complexity: O(n)
Space Complexity: O(1)
</details>

<details>
<summary>Explanation</summary>
The time complexity is O(n) because the function iterates through a loop n times. The space complexity is O(1) because it only uses a constant amount of extra space (the 'total' variable) regardless of the input size.
</details>

## Question 2

What is the time and space complexity of the given code below:

```python
def find_max(arr):
    if not arr:
        return None
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val
```

<details>
<summary>Answer</summary>
Time Complexity: O(n)
Space Complexity: O(1)
</details>

<details>
<summary>Explanation</summary>
The time complexity is O(n) because the function iterates through the entire array once. The space complexity is O(1) because it only uses a constant amount of extra space (the 'max_val' variable) regardless of the input size.
</details>

## Question 3

What is the time and space complexity of the given code below:

```python
def create_matrix(n):
    matrix = []
    for i in range(n):
        row = [0] * n
        matrix.append(row)
    return matrix
```

<details>
<summary>Answer</summary>
Time Complexity: O(n^2)
Space Complexity: O(n^2)
</details>

<details>
<summary>Explanation</summary>
The time complexity is O(n^2) because there are two nested operations: the outer loop runs n times, and for each iteration, it creates a list of size n. The space complexity is also O(n^2) because it creates a matrix of size n x n.
</details>

## Question 4

What is the time and space complexity of the given code below:

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
<summary>Answer</summary>
Time Complexity: O(log n)
Space Complexity: O(1)
</details>

<details>
<summary>Explanation</summary>
The time complexity is O(log n) because the binary search algorithm halves the search space in each iteration. The space complexity is O(1) because it only uses a constant amount of extra space regardless of the input size.
</details>

## Question 5

What is the time and space complexity of the given code below:

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
```

<details>
<summary>Answer</summary>
Time Complexity: O(n)
Space Complexity: O(n)
</details>

<details>
<summary>Explanation</summary>
The time complexity is O(n) because the function makes n recursive calls. The space complexity is O(n) because of the call stack used in recursion, which can go up to n levels deep.
</details>

## Question 6

What is the time and space complexity of the given code below:

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
```

<details>
<summary>Answer</summary>
Time Complexity: O(n^2)
Space Complexity: O(1)
</details>

<details>
<summary>Explanation</summary>
The time complexity is O(n^2) due to the nested loops. The outer loop runs n times, and for each iteration, the inner loop runs n-i-1 times. The space complexity is O(1) because it sorts the array in-place without using any extra space that grows with the input size.
</details>

## Question 7

What is the time and space complexity of the given code below:

```python
def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent % 2 == 0:
        half_power = power(base, exponent // 2)
        return half_power * half_power
    else:
        half_power = power(base, (exponent - 1) // 2)
        return base * half_power * half_power
```

<details>
<summary>Answer</summary>
Time Complexity: O(log n)
Space Complexity: O(log n)
</details>

<details>
<summary>Explanation</summary>
The time complexity is O(log n) because the exponent is halved in each recursive call. The space complexity is O(log n) due to the recursion stack, which goes log n levels deep.
</details>

## Question 8

What is the time and space complexity of the given code below:

```python
def count_elements(arr):
    count_dict = {}
    for num in arr:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    return count_dict
```

<details>
<summary>Answer</summary>
Time Complexity: O(n)
Space Complexity: O(n)
</details>

<details>
<summary>Explanation</summary>
The time complexity is O(n) because it iterates through the array once. The space complexity is O(n) in the worst case, where all elements in the array are unique, resulting in a dictionary with n key-value pairs.
</details>

## Question 9

What is the time and space complexity of the given code below:

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

<details>
<summary>Answer</summary>
Time Complexity: O(2^n)
Space Complexity: O(n)
</details>

<details>
<summary>Explanation</summary>
The time complexity is O(2^n) because each call spawns two more calls, creating a binary tree of calls. The space complexity is O(n) due to the recursion stack, which can go up to n levels deep.
</details>

## Question 10

What is the time and space complexity of the given code below:

```python
def is_palindrome(s):
    return s == s[::-1]
```

<details>
<summary>Answer</summary>
Time Complexity: O(n)
Space Complexity: O(n)
</details>

<details>
<summary>Explanation</summary>
The time complexity is O(n) because reversing a string takes linear time. The space complexity is O(n) because creating a reversed copy of the string requires space proportional to the length of the string.
</details>

## Question 11

What is the time and space complexity of the given code below:

```python
def find_duplicates(arr):
    seen = set()
    duplicates = set()
    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)
```

<details>
<summary>Answer</summary>
Time Complexity: O(n)
Space Complexity: O(n)
</details>

<details>
<summary>Explanation</summary>
The time complexity is O(n) as it iterates through the array once. The space complexity is O(n) in the worst case, where all elements are unique (for the 'seen' set) or all elements are duplicates (for both sets).
</details>

## Question 12

What is the time and space complexity of the given code below:

```python
def matrix_multiplication(A, B):
    n = len(A)
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
    return result
```

<details>
<summary>Answer</summary>
Time Complexity: O(n^3)
Space Complexity: O(n^2)
</details>

<details>
<summary>Explanation</summary>
The time complexity is O(n^3) due to the three nested loops. The space complexity is O(n^2) for storing the result matrix.
</details>

## Question 13

What is the time and space complexity of the given code below:

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
```

<details>
<summary>Answer</summary>
Time Complexity: O(n log n) average case, O(n^2) worst case
Space Complexity: O(n)
</details>

<details>
<summary>Explanation</summary>
The average time complexity is O(n log n) as the array is partitioned log n times, and each partition takes O(n) time. The worst-case time complexity is O(n^2) when the pivot is always the smallest or largest element. The space complexity is O(n) due to the recursive calls and the creation of new lists in each call.
</details>

## Question 14

What is the time and space complexity of the given code below:

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
<summary>Answer</summary>
Time Complexity: O(n + k), where k is the range of input
Space Complexity: O(n + k)
</details>

<details>
<summary>Explanation</summary>
The time complexity is O(n + k) where n is the number of elements in the input array and k is the range of input (max_val + 1). We iterate through the array twice and once through the count array. The space complexity is O(n + k) for the count array and the output array.
</details>

## Question 15

What is the time and space complexity of the given code below:

```python
def longest_common_subsequence(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]
```

<details>
<summary>Answer</summary>
Time Complexity: O(mn)
Space Complexity: O(mn)
</details>

<details>
<summary>Explanation</summary>
The time complexity is O(mn) due to the nested loops iterating over the lengths of both strings. The space complexity is O(mn) for the 2D DP table used to store intermediate results.
</details>

## Question 16

What is the time and space complexity of the given code below:

```python
def generate_permutations(arr):
    if len(arr) <= 1:
        return [arr]
    result = []
    for i in range(len(arr)):
        rest = arr[:i] + arr[i+1:]
        for perm in generate_permutations(rest):
            result.append([arr[i]] + perm)
    return result
```

<details>
<summary>Answer</summary>
Time Complexity: O(n!)
Space Complexity: O(n!)
</details>

<details>
<summary>Explanation</summary>
The time complexity is O(n!) because there are n! permutations for an array of length n. The space complexity is also O(n!) to store all the permutations.
</details>

## Question 17

What is the time and space complexity of the given code below:

```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

<details>
<summary>Answer</summary>
Time Complexity: O(√n)
Space Complexity: O(1)
</details>

<details>
<summary>Explanation</summary>
The time complexity is O(√n) because we only check divisibility up to the square root of n. The space complexity is O(1) as we only use a constant amount of extra space.
</details>

## Question 18

What is the time and space complexity of the given code below:

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

<details>
<summary>Answer</summary>
Time Complexity: O(n log n)
Space Complexity: O(n)
</details>

<details>
<summary>Explanation</summary>
The time complexity is O(n log n) because the array is divided log n times, and each division involves merging, which takes O(n) time. The space complexity is O(n) due to the temporary arrays created during the merge process.
</details>

## Question 19

What is the time and space complexity of the given code below:

```python
def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
```

<details>
<summary>Answer</summary>
Time Complexity: O(n^2)
Space Complexity: O(n)
</details>

<details>
<summary>Explanation</summary>
The time complexity is O(n^2) due to the nested loops. The outer loop runs n times, and for each iteration, the inner loop can run up to i times. The space complexity is O(n) for the dp array used to store intermediate results.
</details>

## Question 20

What is the time and space complexity of the given code below:

```python
def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][capacity]
```

<details>
<summary>Answer</summary>
Time Complexity: O(n * capacity)
Space Complexity: O(n * capacity)
</details>

<details>
<summary>Explanation</summary>
The time complexity is O(n * capacity) because of the two nested loops iterating over n items and capacity weights. The space complexity is also O(n * capacity) for the 2D DP table used to store intermediate results.
</details>

## Question 21

What is the time and space complexity of the given code below:

```python
def count_islands(grid):
    if not grid:
        return 0
    
    def dfs(i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
            return
        grid[i][j] = '0'
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)
    
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(i, j)
                count += 1
    return count
```

<details>
<summary>Answer</summary>
Time Complexity: O(m * n)
Space Complexity: O(m * n)
</details>

<details>
<summary>Explanation</summary>
The time complexity is O(m * n), where m is the number of rows and n is the number of columns in the grid. Each cell is visited at most once. The space complexity is O(m * n) in the worst case due to the recursion stack if the entire grid is filled with land.
</details>

## Question 22

What is the time and space complexity of the given code below:

```python
def rabin_karp(text, pattern):
    n, m = len(text), len(pattern)
    d, q = 256, 101  # d is the number of characters in the alphabet, q is a prime number
    h, p, t = 1, 0, 0
    result = []

    for i in range(m-1):
        h = (h * d) % q

    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(n - m + 1):
        if p == t:
            if text[i:i+m] == pattern:
                result.append(i)
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t += q

    return result
```

<details>
<summary>Answer</summary>
Time Complexity: O(n + m) average case, O(nm) worst case
Space Complexity: O(1)
</details>

<details>
<summary>Explanation</summary>
The average time complexity is O(n + m) where n is the length of the text and m is the length of the pattern. In the worst case (when all characters match but the last one doesn't), it becomes O(nm). The space complexity is O(1) as it uses a constant amount of extra space regardless of input size.
</details>

## Question 23

What is the time and space complexity of the given code below:

```python
def floyd_warshall(graph):
    n = len(graph)
    dist = [row[:] for row in graph]
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist
```

<details>
<summary>Answer</summary>
Time Complexity: O(n^3)
Space Complexity: O(n^2)
</details>

<details>
<summary>Explanation</summary>
The time complexity is O(n^3) due to the three nested loops, each iterating n times. The space complexity is O(n^2) for storing the distance matrix.
</details>

## Question 24

What is the time and space complexity of the given code below:

```python
def generate_subsets(nums):
    def backtrack(start, path):
        result.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
    
    result = []
    backtrack(0, [])
    return result
```

<details>
<summary>Answer</summary>
Time Complexity: O(2^n)
Space Complexity: O(n)
</details>

<details>
<summary>Explanation</summary>
The time complexity is O(2^n) because there are 2^n possible subsets for n elements. The space complexity is O(n) due to the recursion stack and the space needed to store each subset.
</details>

## Question 25

What is the time and space complexity of the given code below:

```python
def count_sort(arr):
    max_val = max(arr)
    min_val = min(arr)
    range_of_values = max_val - min_val + 1
    
    count = [0] * range_of_values
    
    for num in arr:
        count[num - min_val] += 1
    
    output = []
    for i in range(range_of_values):
        output.extend([i + min_val] * count[i])
    
    return output
```

<details>
<summary>Answer</summary>
Time Complexity: O(n + k)
Space Complexity: O(n + k)
</details>

<details>
<summary>Explanation</summary>
The time complexity is O(n + k), where n is the number of elements in the input array and k is the range of values (max_val - min_val + 1). We iterate through the array twice and once through the count array. The space complexity is O(n + k) for the count array and the output array.
</details>

## Question 26

What is the time and space complexity of the given code below:

```python
def trie_insert(root, word):
    node = root
    for char in word:
        if char not in node:
            node[char] = {}
        node = node[char]
    node['#'] = True

def build_trie(words):
    trie = {}
    for word in words:
        trie_insert(trie, word)
    return trie
```

<details>
<summary>Answer</summary>
Time Complexity: O(n * m)
Space Complexity: O(n * m)
</details>

<details>
<summary>Explanation</summary>
The time complexity is O(n * m), where n is the number of words and m is the average length of the words. Each word is inserted into the trie, and each character of the word is processed once. The space complexity is also O(n * m) in the worst case, where there are no common prefixes among the words.
</details>

## Question 27

What is the time and space complexity of the given code below:

```python
def boyer_moore_majority_vote(nums):
    candidate = None
    count = 0
    
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    
    return candidate
```

<details>
<summary>Answer</summary>
Time Complexity: O(n)
Space Complexity: O(1)
</details>

<details>
<summary>Explanation</summary>
The time complexity is O(n) as we iterate through the array once. The space complexity is O(1) because we only use a constant amount of extra space regardless of the input size.
</details>

## Question 28

What is the time and space complexity of the given code below:

```python
def longest_palindromic_substring(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    start, max_length = 0, 1
    
    for i in range(n):
        dp[i][i] = True
    
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if length == 2:
                dp[i][j] = (s[i] == s[j])
            else:
                dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]
            
            if dp[i][j] and length > max_length:
                start = i
                max_length = length
    
    return s[start:start + max_length]
```

<details>
<summary>Answer</summary>
Time Complexity: O(n^2)
Space Complexity: O(n^2)
</details>

<details>
<summary>Explanation</summary>
The time complexity is O(n^2) due to the two nested loops iterating over all possible substring lengths and starting positions. The space complexity is O(n^2) for the 2D DP table used to store intermediate results.
</details>

## Question 29

What is the time and space complexity of the given code below:

```python
def find_bridges(graph):
    def dfs(u, parent):
        nonlocal time
        low[u] = disc[u] = time
        time += 1
        
        for v in graph[u]:
            if v == parent:
                continue
            if disc[v] == -1:
                dfs(v, u)
                low[u] = min(low[u], low[v])
                if low[v] > disc[u]:
                    bridges.append((u, v))
            else:
                low[u] = min(low[u], disc[v])
    
    n = len(graph)
    disc = [-1] * n
    low = [-1] * n
    parent = [-1] * n
    bridges = []
    time = 0
    
    for i in range(n):
        if disc[i] == -1:
            dfs(i, -1)
    
    return bridges
```

<details>
<summary>Answer</summary>
Time Complexity: O(V + E)
Space Complexity: O(V)
</details>

<details>
<summary>Explanation</summary>
The time complexity is O(V + E), where V is the number of vertices and E is the number of edges in the graph. We perform a DFS traversal of the graph, visiting each vertex and edge once. The space complexity is O(V) for the disc, low, and parent arrays, as well as the recursion stack in the worst case.
</details>

## Question 30

What is the time and space complexity of the given code below:

```python
def matrix_chain_multiplication(p):
    n = len(p) - 1
    m = [[0] * n for _ in range(n)]
    
    for chain_length in range(2, n + 1):
        for i in range(n - chain_length + 1):
            j = i + chain_length - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                cost = m[i][k] + m[k+1][j] + p[i] * p[k+1] * p[j+1]
                if cost < m[i][j]:
                    m[i][j] = cost
    
    return m[0][n-1]
```

<details>
<summary>Answer</summary>
Time Complexity: O(n^3)
Space Complexity: O(n^2)
</details>

<details>
<summary>Explanation</summary>
The time complexity is O(n^3) due to the three nested loops: the outer loop for chain length, the middle loop for the starting matrix, and the inner loop for the split point. The space complexity is O(n^2) for the 2D DP table used to store intermediate results.
</details>

## Question 31

What is the time and space complexity of the given code below:

```python
def edit_distance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    
    return dp[m][n]
```

<details>
<summary>Answer</summary>
Time Complexity: O(mn)
Space Complexity: O(mn)
</details>

<details>
<summary>Explanation</summary>
The time complexity is O(mn), where m and n are the lengths of word1 and word2 respectively. We fill a 2D DP table of size (m+1) x (n+1). The space complexity is also O(mn) for storing this DP table.
</details>

## Question 32

What is the time and space complexity of the given code below:

```python
def maximum_subarray_sum(arr):
    max_sum = float('-inf')
    current_sum = 0
    
    for num in arr:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum
```

<details>
<summary>Answer</summary>
Time Complexity: O(n)
Space Complexity: O(1)
</details>

<details>
<summary>Explanation</summary>
The time complexity is O(n) as we iterate through the array once. The space complexity is O(1) because we only use a constant amount of extra space regardless of the input size.
</details>

## Question 33

What is the time and space complexity of the given code below:

```python
def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False
    
    return [i for i in range(2, n+1) if primes[i]]
```

<details>
<summary>Answer</summary>
Time Complexity: O(n log log n)
Space Complexity: O(n)
</details>

<details>
<summary>Explanation</summary>
The time complexity is O(n log log n). The outer loop runs up to √n, and the inner loop runs approximately n/i times for each i. The sum of these operations leads to n log log n. The space complexity is O(n) for the boolean array and the final list of primes.
</details>

## Question 34

What is the time and space complexity of the given code below:

```python
def dijkstra(graph, start):
    n = len(graph)
    distances = [float('inf')] * n
    distances[start] = 0
    pq = [(0, start)]
    
    while pq:
        current_dist, current_node = heapq.heappop(pq)
        
        if current_dist > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances
```

<details>
<summary>Answer</summary>
Time Complexity: O((V + E) log V)
Space Complexity: O(V)
</details>

<details>
<summary>Explanation</summary>
The time complexity is O((V + E) log V), where V is the number of vertices and E is the number of edges. Each vertex is added to and removed from the priority queue once, which takes O(log V) time. Each edge is considered once. The space complexity is O(V) for the distances array and the priority queue.
</details>

## Question 35

What is the time and space complexity of the given code below:

```python
def kmp_search(text, pattern):
    def compute_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            elif length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
        return lps
    
    lps = compute_lps(pattern)
    i = j = 0
    results = []
    
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == len(pattern):
            results.append(i - j)
            j = lps[j - 1]
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    return results
```

<details>
<summary>Answer</summary>
Time Complexity: O(n + m)
Space Complexity: O(m)
</details>

<details>
<summary>Explanation</summary>
The time complexity is O(n + m), where n is the length of the text and m is the length of the pattern. The LPS array computation takes O(m) time, and the main search process takes O(n) time. The space complexity is O(m) for storing the LPS array.
</details>

## Question 36

What is the time and space complexity of the given code below:

```python
def longest_common_substring(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_length = 0
    end_pos = 0
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_pos = i
    
    return s1[end_pos - max_length:end_pos]
```

<details>
<summary>Answer</summary>
Time Complexity: O(mn)
Space Complexity: O(mn)
</details>

<details>
<summary>Explanation</summary>
The time complexity is O(mn), where m and n are the lengths of s1 and s2 respectively. We fill a 2D DP table of size (m+1) x (n+1). The space complexity is also O(mn) for storing this DP table.
</details>

## Question 37

What is the time and space complexity of the given code below:

```python
def topological_sort(graph):
    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        result.append(node)
    
    visited = set()
    result = []
    
    for node in graph:
        if node not in visited:
            dfs(node)
    
    return result[::-1]
```

<details>
<summary>Answer</summary>
Time Complexity: O(V + E)
Space Complexity: O(V)
</details>

<details>
<summary>Explanation</summary>
The time complexity is O(V + E), where V is the number of vertices and E is the number of edges. We visit each vertex once and explore all its edges. The space complexity is O(V) for the visited set, the result list, and the recursion stack in the worst case.
</details>

## Question 38

What is the time and space complexity of the given code below:

```python
def count_inversions(arr):
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr, 0
        mid = len(arr) // 2
        left, inv_left = merge_sort(arr[:mid])
        right, inv_right = merge_sort(arr[mid:])
        merged, inv_merge = merge(left, right)
        return merged, inv_left + inv_right + inv_merge
    
    def merge(left, right):
        result = []
        i = j = inv_count = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
                inv_count += len(left) - i
        result.extend(left[i:])
        result.extend(right[j:])
        return result, inv_count
    
    _, inversions = merge_sort(arr)
    return inversions
```

<details>
<summary>Answer</summary>
Time Complexity: O(n log n)
Space Complexity: O(n)
</details>

<details>
<summary>Explanation</summary>
The time complexity is O(n log n) because we're using a merge sort algorithm. The array is divided log n times, and each division involves merging, which takes O(n) time. The space complexity is O(n) for the temporary arrays created during the merge process.
</details>

## Question 39

What is the time and space complexity of the given code below:

```python
def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [1] * n
    prev = [-1] * n
    
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j
    
    max_length = max(dp)
    last_index = dp.index(max_length)
    
    lis = []
    while last_index != -1:
        lis.append(arr[last_index])
        last_index = prev[last_index]
    
    return lis[::-1]
```

<details>
<summary>Answer</summary>
Time Complexity: O(n^2)
Space Complexity: O(n)
</details>

<details>
<summary>Explanation</summary>
The time complexity is O(n^2) due to the nested loops. For each element, we potentially compare it with all previous elements. The space complexity is O(n) for the dp and prev arrays, as well as the lis list in the worst case.
</details>

## Question 40

What is the time and space complexity of the given code below:

```python
def bellman_ford(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
    
    for node in graph:
        for neighbor, weight in graph[node].items():
            if distances[node] + weight < distances[neighbor]:
                return None  # Negative cycle detected
    
    return distances
```

<details>
<summary>Answer</summary>
Time Complexity: O(VE)
Space Complexity: O(V)
</details>

<details>
<summary>Explanation</summary>
The time complexity is O(VE), where V is the number of vertices and E is the number of edges. We have two nested loops that iterate V-1 times over all edges. The space complexity is O(V) for storing the distances dictionary.
</details>

## Question 41

What is the time and space complexity of the given code below:

```python
def count_prime_factors(n):
    factors = 0
    d = 2
    while n > 1:
        while n % d == 0:
            factors += 1
            n //= d
        d += 1
        if d * d > n:
            if n > 1:
                factors += 1
            break
    return factors
```

<details>
<summary>Answer</summary>
Time Complexity: O(√n)
Space Complexity: O(1)
</details>

<details>
<summary>Explanation</summary>
The time complexity is O(√n) because we only need to check factors up to the square root of n. Once d * d > n, if n is still greater than 1, it must be prime. The space complexity is O(1) as we only use a constant amount of extra space.
</details>

## Question 42

What is the time and space complexity of the given code below:

```python
def max_profit(prices):
    if not prices:
        return 0
    
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    
    return max_profit
```

<details>
<summary>Answer</summary>
Time Complexity: O(n)
Space Complexity: O(1)
</details>

<details>
<summary>Explanation</summary>
The time complexity is O(n) where n is the number of prices, as we iterate through the list once. The space complexity is O(1) because we only use a constant amount of extra space regardless of the input size.
</details>

## Question 43

What is the time and space complexity of the given code below:

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
<summary>Answer</summary>
Time Complexity: O(n^2)
Space Complexity: O(n^2)
</details>

<details>
<summary>Explanation</summary>
The time complexity is O(n^2) due to the nested loops iterating over all possible substring lengths and starting positions. The space complexity is O(n^2) for the 2D DP table used to store intermediate results.
</details>

## Question 44

What is the time and space complexity of the given code below:

```python
def find_kth_largest(nums, k):
    def quickselect(l, r):
        pivot, p = nums[r], l
        for i in range(l, r):
            if nums[i] <= pivot:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1
        nums[p], nums[r] = nums[r], nums[p]
        
        if k < len(nums) - p:
            return quickselect(p + 1, r)
        elif k > len(nums) - p:
            return quickselect(l, p - 1)
        else:
            return nums[p]
    
    return quickselect(0, len(nums) - 1)
```

<details>
<summary>Answer</summary>
Time Complexity: O(n) average case, O(n^2) worst case
Space Complexity: O(1)
</details>

<details>
<summary>Explanation</summary>
The average time complexity is O(n) because on average, we eliminate half of the remaining elements in each recursion. In the worst case (when the pivot is always the smallest or largest element), it becomes O(n^2). The space complexity is O(1) as it sorts in-place and the recursion depth is O(1) on average.
</details>

## Question 45

What is the time and space complexity of the given code below:

```python
def count_bits(n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i >> 1] + (i & 1)
    return dp
```

<details>
<summary>Answer</summary>
Time Complexity: O(n)
Space Complexity: O(n)
</details>

<details>
<summary>Explanation</summary>
The time complexity is O(n) as we iterate from 1 to n once. The space complexity is O(n) for storing the dp array which has n+1 elements.
</details>

## Question 46

What is the time and space complexity of the given code below:

```python
def largest_rectangle_area(heights):
    stack = [-1]
    heights.append(0)
    max_area = 0
    
    for i, h in enumerate(heights):
        while heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    
    return max_area
```

<details>
<summary>Answer</summary>
Time Complexity: O(n)
Space Complexity: O(n)
</details>

<details>
<summary>Explanation</summary>
The time complexity is O(n) where n is the number of heights. Although there's a while loop inside the for loop, each element is pushed and popped at most once, so the amortized time complexity is O(n). The space complexity is O(n) for the stack in the worst case when the heights are in ascending order.
</details>

## Question 47

What is the time and space complexity of the given code below:

```python
def max_sliding_window(nums, k):
    from collections import deque
    
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
<summary>Answer</summary>
Time Complexity: O(n)
Space Complexity: O(k)
</details>

<details>
<summary>Explanation</summary>
The time complexity is O(n) where n is the length of nums. Although there are while loops inside the for loop, each element is added and removed from the deque at most once. The space complexity is O(k) for the deque, which stores at most k elements.
</details>

## Question 48

What is the time and space complexity of the given code below:

```python
def min_distance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
    
    return dp[m][n]
```

<details>
<summary>Answer</summary>
Time Complexity: O(mn)
Space Complexity: O(mn)
</details>

<details>
<summary>Explanation</summary>
The time complexity is O(mn) where m and n are the lengths of word1 and word2 respectively. We fill a 2D DP table of size (m+1) x (n+1). The space complexity is also O(mn) for storing this DP table.
</details>

## Question 49

What is the time and space complexity of the given code below:

```python
def count_smaller(nums):
    def merge_sort(enum):
        half = len(enum) // 2
        if half:
            left, right = merge_sort(enum[:half]), merge_sort(enum[half:])
            for i in range(len(enum))[::-1]:
                if not right or left and left[-1][1] > right[-1][1]:
                    smaller[left[-1][0]] += len(right)
                    enum[i] = left.pop()
                else:
                    enum[i] = right.pop()
        return enum
    
    smaller = [0] * len(nums)
    merge_sort(list(enumerate(nums)))
    return smaller
```

<details>
<summary>Answer</summary>
Time Complexity: O(n log n)
Space Complexity: O(n)
</details>

<details>
<summary>Explanation</summary>
The time complexity is O(n log n) as this is a modified merge sort algorithm. The array is divided log n times, and each division involves merging, which takes O(n) time. The space complexity is O(n) for the temporary arrays created during the merge process and the smaller array.
</details>

## Question 50

What is the time and space complexity of the given code below:

```python
def calculate(s):
    stack = []
    num = 0
    sign = '+'
    
    for i, char in enumerate(s + '+'):
        if char.isdigit():
            num = num * 10 + int(char)
        elif char in '+-*/':
            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            elif sign == '*':
                stack.append(stack.pop() * num)
            elif sign == '/':
                stack.append(int(stack.pop() / num))
            num = 0
            sign = char
    
    return sum(stack)
```

<details>
<summary>Answer</summary>
Time Complexity: O(n)
Space Complexity: O(n)
</details>

<details>
<summary>Explanation</summary>
The time complexity is O(n) where n is the length of the string s. We iterate through each character once. The space complexity is O(n) in the worst case for the stack, which could potentially store all numbers in the expression if they're all addition or subtraction operations.
</details>
