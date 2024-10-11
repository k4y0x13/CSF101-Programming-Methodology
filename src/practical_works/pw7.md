# Practical Work VII

# Practical 7: Binary Search Tree Implementation
**Due Date:** [Specify date]
**Submission:** GitHub repository link containing:
- Python source code (.py file)
- Lab report in markdown format
- Test cases file

## Learning Objectives
- Understand Binary Search Tree (BST) data structure
- Implement basic BST operations
- Practice recursive algorithms
- Learn tree traversal techniques
- Apply proper testing strategies

## Requirements
Create a Python program that implements a Binary Search Tree with the following operations:
1. Node creation
2. Insertion of nodes
3. Searching for a value
4. Deletion of nodes
5. Tree traversals (in-order, pre-order, post-order)
6. Basic tree statistics (height, node count)

## Step-by-Step Implementation Guide

### Step 1: Create Node Class
1. Create a new Python file named `binary_search_tree.py`
2. Implement the Node class:
```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
```

### Step 2: Create BST Class Structure
1. Implement the basic BST class:
```python
class BinarySearchTree:
    def __init__(self):
        self.root = None
```

### Step 3: Implement Insertion
1. Create the insert method:
```python
def insert(self, value):
    if self.root is None:
        self.root = Node(value)
    else:
        self._insert_recursive(self.root, value)

def _insert_recursive(self, node, value):
    if value < node.value:
        if node.left is None:
            node.left = Node(value)
        else:
            self._insert_recursive(node.left, value)
    else:
        if node.right is None:
            node.right = Node(value)
        else:
            self._insert_recursive(node.right, value)
```

### Step 4: Implement Search
1. Add search functionality:
```python
def search(self, value):
    return self._search_recursive(self.root, value)

def _search_recursive(self, node, value):
    if node is None or node.value == value:
        return node
    
    if value < node.value:
        return self._search_recursive(node.left, value)
    return self._search_recursive(node.right, value)
```

### Step 5: Implement Tree Traversals
1. Add in-order traversal:
```python
def inorder_traversal(self):
    result = []
    self._inorder_recursive(self.root, result)
    return result

def _inorder_recursive(self, node, result):
    if node:
        self._inorder_recursive(node.left, result)
        result.append(node.value)
        self._inorder_recursive(node.right, result)
```

2. Add pre-order traversal:
```python
def preorder_traversal(self):
    result = []
    self._preorder_recursive(self.root, result)
    return result

def _preorder_recursive(self, node, result):
    if node:
        result.append(node.value)
        self._preorder_recursive(node.left, result)
        self._preorder_recursive(node.right, result)
```

3. Add post-order traversal:
```python
def postorder_traversal(self):
    result = []
    self._postorder_recursive(self.root, result)
    return result

def _postorder_recursive(self, node, result):
    if node:
        self._postorder_recursive(node.left, result)
        self._postorder_recursive(node.right, result)
        result.append(node.value)
```

### Step 6: Implement Deletion
1. Add node deletion functionality:
```python
def delete(self, value):
    self.root = self._delete_recursive(self.root, value)

def _delete_recursive(self, node, value):
    if node is None:
        return None
    
    if value < node.value:
        node.left = self._delete_recursive(node.left, value)
    elif value > node.value:
        node.right = self._delete_recursive(node.right, value)
    else:
        # Node with only one child or no child
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        
        # Node with two children
        # Get the inorder successor (smallest in right subtree)
        temp = self._min_value_node(node.right)
        node.value = temp.value
        node.right = self._delete_recursive(node.right, temp.value)
    
    return node

def _min_value_node(self, node):
    current = node
    while current.left:
        current = current.left
    return current
```

### Step 7: Implement Tree Statistics
1. Add methods to calculate tree height and node count:
```python
def get_height(self):
    return self._get_height_recursive(self.root)

def _get_height_recursive(self, node):
    if node is None:
        return 0
    left_height = self._get_height_recursive(node.left)
    right_height = self._get_height_recursive(node.right)
    return max(left_height, right_height) + 1

def get_node_count(self):
    return self._get_node_count_recursive(self.root)

def _get_node_count_recursive(self, node):
    if node is None:
        return 0
    return 1 + self._get_node_count_recursive(node.left) + \
           self._get_node_count_recursive(node.right)
```

### Step 8: Main Program and Testing
1. Create a main program to test all operations:
```python
def main():
    bst = BinarySearchTree()
    
    # Test insertion
    values = [50, 30, 70, 20, 40, 60, 80]
    for value in values:
        bst.insert(value)
    
    # Test traversals
    print("In-order traversal:", bst.inorder_traversal())
    print("Pre-order traversal:", bst.preorder_traversal())
    print("Post-order traversal:", bst.postorder_traversal())
    
    # Test search
    print("Searching for 40:", "Found" if bst.search(40) else "Not found")
    print("Searching for 90:", "Found" if bst.search(90) else "Not found")
    
    # Test statistics
    print("Tree height:", bst.get_height())
    print("Node count:", bst.get_node_count())
    
    # Test deletion
    bst.delete(30)
    print("After deleting 30, in-order traversal:", bst.inorder_traversal())

if __name__ == "__main__":
    main()
```

## Testing Instructions
1. Create test cases for:
   - Empty tree operations
   - Single node operations
   - Balanced tree operations
   - Unbalanced tree operations
   - Edge cases (duplicates, missing values)

2. Test each operation:
   - Insertion of various values
   - Search for existing and non-existing values
   - Deletion of leaf nodes, nodes with one child, and nodes with two children
   - All three traversal methods
   - Height and node count calculations

## Expected Output Format
```
Binary Search Tree Operations Test
--------------------------------
Initial tree values: [50, 30, 70, 20, 40, 60, 80]

Traversals:
In-order: [20, 30, 40, 50, 60, 70, 80]
Pre-order: [50, 30, 20, 40, 70, 60, 80]
Post-order: [20, 40, 30, 60, 80, 70, 50]

Search Tests:
Value 40: Found
Value 90: Not found

Tree Statistics:
Height: 3
Node Count: 7

After deletion of 30:
In-order: [20, 40, 50, 60, 70, 80]
```

## Grading Criteria Breakdown
### Executability (3 points)
- Program runs without errors (1.5)
- All operations work correctly (1.5)

### Instruction Compliance (2 points)
- All required methods implemented (1)
- Proper class structure and naming (1)

### Solution Approach (2 points)
- Efficient implementation (1)
- Proper recursion usage (1)

### Data Structure Usage (2 points)
- Correct BST properties maintained (1)
- Proper node relationships (1)

### Submission Timeliness (1 point)
- Submitted before deadline on GitHub (1)

## Submission Requirements
1. In your `ProgrammingPracticals` repository:
   - `binary_search_tree.py`
   - `lab_report.md`
   - `test_cases.py`
   - Updated README.md

## Lab Report Template
Your lab report should include:
1. Introduction to BST and its applications
2. Implementation approach and design decisions
3. Challenges faced in implementation
4. Test cases and results
5. Time complexity analysis of operations
6. Conclusions and learning outcomes

## Additional Resources
- Binary Search Tree visualization tools
- Python recursion tutorials
- Tree traversal animations
- Time complexity analysis of BST operations
