# Practical Work IX

# Practical 9: Graph Implementation and Traversal
**Due Date:** [Specify date]
**Submission:** GitHub repository link containing:
- Python source code (.py file)
- Lab report in markdown format
- Test cases documentation

## Learning Objectives
- Understand graph data structure concepts
- Implement an adjacency list representation
- Master basic graph traversal algorithms (BFS and DFS)
- Practice using dictionaries and lists in Python
- Learn queue and stack usage in graph traversal

## Requirements
Create a Python program that:
1. Implements a graph using adjacency list
2. Provides methods to add vertices and edges
3. Implements Depth-First Search (DFS)
4. Implements Breadth-First Search (BFS)
5. Allows for testing with different graph configurations

## Step-by-Step Implementation Guide

### Step 1: Basic Graph Class
1. Create a new Python file named `graph.py`
2. Implement the basic Graph class using a dictionary for the adjacency list:

```python
class Graph:
    def __init__(self):
        # Initialize an empty dictionary to store the graph
        self.graph = {}
    
    def add_vertex(self, vertex):
        # Add a vertex if it's not already in the graph
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, vertex1, vertex2):
        # Add edge from vertex1 to vertex2
        if vertex1 in self.graph:
            if vertex2 not in self.graph[vertex1]:
                self.graph[vertex1].append(vertex2)
        else:
            self.graph[vertex1] = [vertex2]
        
        # Add vertices if they don't exist
        if vertex2 not in self.graph:
            self.graph[vertex2] = []
    
    def display(self):
        # Display the adjacency list
        for vertex in self.graph:
            print(f"{vertex}: {self.graph[vertex]}")
```

### Step 2: Depth-First Search Implementation
1. Add the DFS method to the Graph class:

```python
def dfs(self, start_vertex):
    # Set to keep track of visited vertices
    visited = set()
    # List to store the traversal order
    traversal = []
    
    def dfs_helper(vertex):
        # Mark vertex as visited
        visited.add(vertex)
        # Add to traversal list
        traversal.append(vertex)
        
        # Visit all adjacent vertices
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                dfs_helper(neighbor)
    
    # Start DFS from the start vertex
    dfs_helper(start_vertex)
    return traversal
```

### Step 3: Breadth-First Search Implementation
1. Import the queue module
2. Add the BFS method to the Graph class:

```python
from collections import deque

def bfs(self, start_vertex):
    # Set to keep track of visited vertices
    visited = set()
    # Queue for BFS
    queue = deque([start_vertex])
    # List to store the traversal order
    traversal = []
    
    # Start with the start_vertex
    visited.add(start_vertex)
    
    while queue:
        # Remove and return first vertex from queue
        vertex = queue.popleft()
        traversal.append(vertex)
        
        # Add all unvisited neighbors to queue
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return traversal
```

### Step 4: Main Program and Testing
1. Create a main section to test the graph:

```python
def main():
    # Create a new graph
    g = Graph()
    
    # Add vertices
    vertices = ['A', 'B', 'C', 'D', 'E']
    for vertex in vertices:
        g.add_vertex(vertex)
    
    # Add edges to create a sample graph
    edges = [
        ('A', 'B'), ('A', 'C'),
        ('B', 'D'), ('C', 'D'),
        ('D', 'E')
    ]
    for v1, v2 in edges:
        g.add_edge(v1, v2)
    
    # Display the graph
    print("Graph Adjacency List:")
    g.display()
    
    # Test DFS
    print("\nDFS starting from vertex 'A':")
    print(g.dfs('A'))
    
    # Test BFS
    print("\nBFS starting from vertex 'A':")
    print(g.bfs('A'))

if __name__ == "__main__":
    main()
```

## Testing Instructions
1. Create test cases with different graph configurations:
   - Small graph (5-6 vertices)
   - Medium graph (10-12 vertices)
   - Disconnected graph
   - Cyclic graph

2. Test each graph with both DFS and BFS from different starting vertices

### Sample Test Cases
```python
def test_cases():
    g = Graph()
    
    # Test Case 1: Simple linear graph
    print("Test Case 1: Linear Graph")
    vertices = [1, 2, 3, 4, 5]
    edges = [(1,2), (2,3), (3,4), (4,5)]
    
    for v in vertices:
        g.add_vertex(v)
    for v1, v2 in edges:
        g.add_edge(v1, v2)
    
    print("DFS:", g.dfs(1))
    print("BFS:", g.bfs(1))
    
    # Test Case 2: Cyclic graph
    # Add more test cases here...
```

## Expected Output Format
```
Graph Adjacency List:
A: ['B', 'C']
B: ['D']
C: ['D']
D: ['E']
E: []

DFS starting from vertex 'A':
['A', 'B', 'D', 'E', 'C']

BFS starting from vertex 'A':
['A', 'B', 'C', 'D', 'E']
```

## Grading Criteria Breakdown
### Executability (3 points)
- Program runs without errors (1.5)
- All traversal algorithms work correctly (1.5)

### Instruction Compliance (2 points)
- All required methods implemented (1)
- Proper file structure and naming (1)

### Solution Approach (2 points)
- Correct implementation of graph structure (1)
- Proper implementation of traversal algorithms (1)

### Data Structure Usage (2 points)
- Appropriate use of adjacency list (1)
- Efficient use of auxiliary data structures (1)

### Submission Timeliness (1 point)
- Submitted before deadline on GitHub (1)

## Submission Requirements
1. In your `ProgrammingPracticals` repository:
   - `graph.py`
   - `lab_report.md`
   - `test_cases.py` (optional but recommended)
2. README.md with:
   - Student information
   - Installation instructions
   - Usage examples
   - Sample output screenshots

## Lab Report Template
Your lab report should include:
1. Introduction to graphs and traversal algorithms
2. Implementation approach and decisions
3. Challenges faced during implementation
4. Test cases and their results
5. Comparative analysis of DFS vs BFS
6. Conclusions and learning outcomes

## Additional Resources
- Graph theory basics
- Python dictionary operations
- Queue and Stack in Python
- Recursive vs Iterative approaches
- Time complexity analysis of graph traversals
