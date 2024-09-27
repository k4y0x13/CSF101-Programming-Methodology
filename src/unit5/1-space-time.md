# Space Time Complexity - Asymptotic Notation

[YouTube Video Explaining Big O](https://www.youtube.com/watch?v=XMUe3zFhM5c)

# Introduction

In the world of computer science, particularly in the study of Data Structures and Algorithms, you'll often hear about "Big O notation." 

# 1. Concept of Time & Space

## 1.1 Time Complexity

Time complexity is a way to **describe how long an algorithm takes to run** _as the input size increases_. It's not about measuring the actual time in seconds, but rather about counting the number of operations the algorithm performs.

Think of it like this: Imagine you're baking cookies. The time complexity would be like counting how many steps (mixing ingredients, shaping cookies, etc.) you need to perform to bake a certain number of cookies. As you bake more cookies, you might need more steps.

**How to express the Time Complexity of an Algorithm:**

We use Big O notation to express time complexity. It describes the **worst-case scenario** or the maximum number of operations an algorithm might need to perform.

Here are some common time complexities, from fastest to slowest:

- O(1) - Constant time
- O(log n) - Logarithmic time
- O(n) - Linear time
- O(n log n) - Linearithmic time
- O(n^2) - Quadratic time
- O(2^n) - Exponential time
- O(n!) - Factorial time

## 1.2 Space Complexity

Space complexity is about **ehow much additional memory an algorithm needs** to run as the input size increases. It's not about the space taken by the input itself, but the extra space the algorithm uses.

Think of it like this: When you're baking cookies, space complexity would be like measuring how many extra bowls, spoons, and baking sheets you need as you make more cookies.

The representation of Space Complexities is the same as that of Time Complexity - using Big O notaiton.

Here are some common time complexities, from fastest to slowest:

- O(1) - Constant space
- O(log n) - Logarithmic space
- O(n) - Linear space
- O(n log n) - Linearithmic space
- O(n^2) - Quadratic space
- O(2^n) - Exponential space
- O(n!) - Factorial space

# 2. Why Big O Notation?

Big O notation is a fundamental concept in computer science for several reasons:

1. **Efficiency Analysis**: It helps us analyze the efficiency of algorithms, allowing us to compare different approaches to solving a problem.

2. **Scalability**: It gives us insight into how an algorithm will perform as the input size grows, which is crucial for building systems that can handle large amounts of data.

3. **Optimization**: Understanding Big O helps developers optimize their code by choosing the most efficient algorithms for their specific use cases.

4. **Standardized Communication**: It provides a standardized way to discuss algorithm performance across the computer science community.

# 3. Best Case, Average Case, and Worst Case

When analyzing algorithms, we often consider three scenarios:

1. **Best Case**: The most favorable input scenario, resulting in the fastest possible execution time.

2. **Average Case**: The expected performance for a typical input.

3. **Worst Case**: The least favorable input scenario, resulting in the slowest execution time.

Big O notation typically describes the worst-case scenario, as it gives us an upper bound on the algorithm's performance. This ensures we're prepared for the most challenging situations our algorithm might face.

# 4. Mathematical Origins (Brief Overview)

Big O notation originated from mathematics, specifically from the field of asymptotic analysis. It was introduced by the German mathematician Paul Bachmann in 1894 and later popularized in computer science.

The "O" in Big O stands for "Order of," referring to the order of magnitude of the algorithm's performance. It describes how the runtime of an algorithm grows relative to the input size as the input size approaches infinity.

While the mathematical foundations are complex, in computer science, we use a simplified version that focuses on the dominant term of the function describing the algorithm's performance.

# 5 Examples - Time & Space Complexity

## 5.1 O(1) Time, O(1) Space - Constant Time and Space

```python
def get_first_element(arr):
    return arr[0] if arr else None

# Usage
result = get_first_element([1, 2, 3, 4, 5])
```

This function always performs one operation (accessing the first element) regardless of the input size, and uses a constant amount of extra space.

## 5.2 O(n) Time, O(1) Space - Linear Time, Constant Space

```python
def find_max(arr):
    if not arr:
        return None
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

# Usage
result = find_max([3, 7, 2, 9, 1])
```

This function iterates through the array once, taking linear time, but uses only a single variable for extra space.

## 5.3 O(n) Time, O(n) Space - Linear Time and Space

```python
def double_array(arr):
    return [num * 2 for num in arr]

# Usage
result = double_array([1, 2, 3, 4, 5])
```

This function creates a new array of the same size as the input, resulting in linear space complexity, and processes each element once for linear time complexity.

## 5.4 O(log n) Time, O(1) Space - Logarithmic Time, Constant Space

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

# Usage
sorted_array = [1, 3, 5, 7, 9, 11, 13, 15]
result = binary_search(sorted_array, 7)
```

Binary search divides the search space in half each time, resulting in logarithmic time complexity. It uses a constant amount of extra space for variables.

## 5.5 O(n log n) Time, O(n) Space - Linearithmic Time, Linear Space

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

# Usage
result = merge_sort([5, 2, 8, 12, 1, 6])
```

Merge sort has linearithmic time complexity due to its divide-and-conquer nature. It uses linear extra space for the merged arrays during the sorting process.

## 5.6 O(n^2) Time, O(1) Space - Quadratic Time, Constant Space

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Usage
result = bubble_sort([64, 34, 25, 12, 22, 11, 90])
```

Bubble sort uses nested loops, resulting in quadratic time complexity. It sorts the array in-place, using only a constant amount of extra space.

## 5.7 O(n^2) Time, O(n^2) Space - Quadratic Time and Space

```python
def create_multiplication_table(n):
    return [[i * j for j in range(1, n+1)] for i in range(1, n+1)]

# Usage
result = create_multiplication_table(5)
```

This function creates a 2D array of size n x n, resulting in quadratic space complexity. It also takes quadratic time to fill the array.

## 5.8 O(2^n) Time, O(n) Space - Exponential Time, Linear Space

```python
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Usage
result = fibonacci_recursive(10)
```

This naive recursive implementation of Fibonacci has exponential time complexity due to redundant calculations. The space complexity is linear due to the call stack depth.

## 5.9 O(n!) Time, O(n) Space - Factorial Time, Linear Space

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

# Usage
result = generate_permutations([1, 2, 3])
```

Generating all permutations has factorial time complexity. The space complexity is linear due to the recursion depth and the storage of partial permutations.

## 5.10 O(n^3) Time, O(1) Space - Cubic Time, Constant Space

```python
def find_triplet_sum(arr, target_sum):
    n = len(arr)
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == target_sum:
                    return (arr[i], arr[j], arr[k])
    return None

# Usage
result = find_triplet_sum([1, 4, 45, 6, 10, 8], 22)
```

This function uses three nested loops to find a triplet with a given sum, resulting in cubic time complexity. It uses only a constant amount of extra space.

## 5.11 O(log log n) Time, O(1) Space - Double Logarithmic Time, Constant Space

```python
def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high and arr[low] <= target <= arr[high]:
        if low == high:
            return low if arr[low] == target else -1
        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])
        if arr[pos] == target:
            return pos
        if arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1

# Usage
sorted_array = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
result = interpolation_search(sorted_array, 64)
```

Interpolation search can achieve O(log log n) time complexity for uniformly distributed data. It uses constant extra space.

## 5.12 O(n + m) Time, O(1) Space - Linear Time (Multiple Inputs), Constant Space

```python
def find_intersection(arr1, arr2):
    i, j = 0, 0
    result = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            result.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
    return result

# Usage
result = find_intersection([1, 3, 4, 6, 7, 9], [1, 2, 4, 5, 9, 10])
```

This function finds the intersection of two sorted arrays in linear time relative to the sum of their lengths. It uses constant extra space.

## 5.13 O(n) Time, O(k) Space - Linear Time, Limited Linear Space

```python
from collections import Counter

def top_k_frequent(arr, k):
    count = Counter(arr)
    return [item for item, _ in count.most_common(k)]

# Usage
result = top_k_frequent([1, 1, 1, 2, 2, 3], 2)
```

This function finds the k most frequent elements in linear time. The space complexity is O(k) for storing the k most frequent elements.

## 5.14 O(V + E) Time, O(V) Space - Linear Time and Space (Graph Algorithms)

```python
from collections import defaultdict, deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    result = []
    
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result

# Usage
graph = defaultdict(list)
graph[0] = [1, 2]
graph[1] = [2]
graph[2] = [0, 3]
graph[3] = [3]
result = bfs(graph, 2)
```

Breadth-First Search (BFS) visits each vertex and edge once, resulting in O(V + E) time complexity. The space complexity is O(V) for the visited set and queue.

## 5.15 O(log n) Time, O(log n) Space - Logarithmic Time and Space

```python
def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

# Usage
sorted_array = [1, 3, 5, 7, 9, 11, 13, 15]
result = binary_search_recursive(sorted_array, 7, 0, len(sorted_array) - 1)
```

This recursive implementation of binary search has logarithmic time complexity. The space complexity is also logarithmic due to the recursion stack.

## 5.16 O(n) Time, O(h) Space - Linear Time, Height Space (Tree Traversal)

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root):
    def inorder(node):
        if not node:
            return
        inorder(node.left)
        result.append(node.val)
        inorder(node.right)
    
    result = []
    inorder(root)
    return result

# Usage
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
result = inorder_traversal(root)
```

Inorder traversal visits each node once (linear time). The space complexity is O(h), where h is the height of the tree, due to the recursion stack.

## 5.17 O(n^2) Time, O(n) Space - Quadratic Time, Linear Space

```python
def longest_palindromic_subsequence(s):
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

# Usage
result = longest_palindromic_subsequence("bbbab")
```

This dynamic programming solution for finding the longest palindromic subsequence has quadratic time complexity due to the nested loops. It uses linear space for the DP table.

## 5.18 O(2^n) Time, O(2^n) Space - Exponential Time and Space

```python
def generate_power_set(arr):
    if not arr:
        return [[]]
    result = generate_power_set(arr[1:])
    return result + [[arr[0]] + subset for subset in result]

# Usage
result = generate_power_set([1, 2, 3])
```

Generating the power set of a set has exponential time and space complexity, as the number of subsets is 2^n for a set of n elements.

## 5.19 O(n * m) Time, O(min(n, m)) Space - Polynomial Time, Limited Linear Space

```python
def levenshtein_distance(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    
    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2+1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
        distances = distances_
    
    return distances[-1]

# Usage
result = levenshtein_distance("kitten", "sitting")
```

This implementation of the Levenshtein distance algorithm has time complexity O(n * m) where n and m are the lengths of the input strings. It uses O(min(n, m)) space by keeping only two rows of the distance matrix at a time.
