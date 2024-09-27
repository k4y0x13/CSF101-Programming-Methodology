# Hash Table Implementations

# Leetcode Lesson: Hash Table Implementation

## 1. Problem Statement

Implement a hash table with the following operations:
- `put(key, value)`: Insert a (key, value) pair into the hash table. If the key already exists, update the corresponding value.
- `get(key)`: Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
- `remove(key)`: Remove the mapping for the value key if this map contains the mapping for the key.

Note:
- All keys and values will be in the range of [0, 1000000].
- The number of operations will be in the range of [1, 10000].
- Please do not use the built-in hash table library.

## 2. Conceptual Understanding

A hash table is a data structure that implements an associative array abstract data type, a structure that can map keys to values. It uses a hash function to compute an index into an array of buckets or slots, from which the desired value can be found.

Think of a hash table like a library catalog system:
- The key is like a book's ISBN number.
- The value is like the book's location in the library.
- The hash function is like the system that converts the ISBN into a shelf number.

## 3. Approach Brainstorming

For implementing a hash table, we need to consider:
1. Choosing a hash function
2. Handling collisions (when two keys hash to the same index)
3. Resizing the table when it becomes too full

Common approaches for handling collisions:
- Chaining: Each bucket is independent, and has some sort of list of entries with the same index.
- Open addressing: All entry records are stored in the bucket array itself.

For this implementation, we'll use chaining with linked lists for simplicity.

## 4. Optimal Solution Walkthrough

1. Create a fixed-size array to store our buckets.
2. Implement a simple hash function that maps keys to indices.
3. Use chaining (linked lists) to handle collisions.
4. Implement put, get, and remove operations.

We'll use a load factor to determine when to resize the hash table, but we won't implement the resizing for simplicity.

## 5. Python Implementation

```python
class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.table = [None] * self.size
    
    def put(self, key: int, value: int) -> None:
        index = key % self.size
        if self.table[index] == None:
            self.table[index] = ListNode(key, value)
        else:
            curr = self.table[index]
            while curr:
                if curr.key == key:
                    curr.value = value
                    return
                if curr.next == None: break
                curr = curr.next
            curr.next = ListNode(key, value)
    
    def get(self, key: int) -> int:
        index = key % self.size
        curr = self.table[index]
        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next
        return -1
    
    def remove(self, key: int) -> None:
        index = key % self.size
        curr = prev = self.table[index]
        if not curr: return
        if curr.key == key:
            self.table[index] = curr.next
        else:
            curr = curr.next
            while curr:
                if curr.key == key:
                    prev.next = curr.next
                    break
                prev, curr = curr, curr.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
```

## 6. Time and Space Complexity Analysis

**Time Complexity**:
- put(): O(1) average case, O(n) worst case
- get(): O(1) average case, O(n) worst case
- remove(): O(1) average case, O(n) worst case

Where n is the number of keys with the same hash value.

**Space Complexity**: O(m + k), where m is the number of buckets and k is the number of unique keys.

## 7. Edge Cases and Testing

Consider these test cases:
- Insert and retrieve a single key-value pair
- Insert multiple key-value pairs with the same key
- Remove a key that doesn't exist
- Get a key that doesn't exist
- Insert many key-value pairs to test collision handling

## 8. Common Pitfalls and Mistakes

- Forgetting to handle collisions
- Not updating the value if the key already exists in put()
- Incorrect handling of the head of the linked list in remove()
- Using a poor hash function that leads to many collisions

## 9. Optimization Opportunities

- Implement resizing to maintain a good load factor
- Use a more sophisticated hash function
- Consider using open addressing instead of chaining for better cache performance

## 10. Related Problems and Concepts

- "Design HashMap" on LeetCode
- "LRU Cache" implementation
- Understanding of linked lists
- Collision resolution techniques in hash tables

## 11. Reflection Questions

1. How would the implementation change if we used open addressing instead of chaining?
2. What are the trade-offs between using a larger initial size for the hash table versus implementing resizing?
3. How might you implement a hash function for string keys instead of integer keys?

## 12. Additional Resources

- [Hash Table on Wikipedia](https://en.wikipedia.org/wiki/Hash_table)
- [Python Dictionary Implementation](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [Collision Resolution Techniques](https://www.geeksforgeeks.org/hashing-set-2-separate-chaining/)
