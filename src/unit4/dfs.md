# Depth-First Search

# Concept

Depth-First Search (DFS) is a fundamental graph traversal algorithm used in computer science and artificial intelligence. It explores a graph or tree data structure by **going as deep as possible** along each branch before backtracking. This approach allows DFS to reach the leaf nodes of a graph quickly, making it useful for many applications such as pathfinding, topological sorting, and cycle detection.

The key characteristic of DFS is its **"depth-first"** nature: it prioritizes exploring as far as possible along each branch before exploring other branches. This behavior is analogous to exploring a maze by following each path to its end before backtracking and trying a different path.

<iframe width="560" height="315" src="https://www.youtube.com/embed/Urx87-NMm6c?si=lXpdEPPMjOMLHuQb" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

# How DFS Works - Recursive & Iterative

## Recursive DFS

The recursive implementation of DFS is elegant and intuitive, mirroring the algorithm's natural depth-first behavior:

1. Start at a chosen node (often called the root in tree structures).
2. Mark the current node as visited.
3. For each unvisited neighbor of the current node:
   a. Recursively apply DFS to that neighbor.
4. If all neighbors are visited, the function returns (effectively backtracking).

This process naturally creates a depth-first traversal as the recursion pushes deeper into the graph before unwinding.

## Iterative DFS

The iterative version uses a stack to simulate the recursive call stack:

1. Start at the chosen node and push it onto a stack.
2. While the stack is not empty:
   a. Pop a node from the stack and mark it as visited.
   b. Push all unvisited neighbors of this node onto the stack.
3. Repeat step 2 until the stack is empty.

The stack ensures that we explore deeper paths before wider ones, maintaining the depth-first property.

# Time / Space Complexity - Recursive and Iterative

## Time Complexity

Both recursive and iterative implementations have the same time complexity:
- O(V + E) for an adjacency list representation
- O(V^2) for an adjacency matrix representation

Where V is the number of vertices and E is the number of edges in the graph.

This is because each vertex and edge will be explored once.

## Space Complexity

### Recursive DFS
- Worst case: O(V) where V is the number of vertices
- This occurs in the case of a skewed graph (like a linked list)
- The space is used by the call stack

### Iterative DFS
- Worst case: O(V) where V is the number of vertices
- This space is used by the explicit stack data structure

In practice, the iterative version often has better space efficiency, especially for very deep graphs, as it avoids potential stack overflow issues.

# When to Use & When Not to Use DFS - Recursive and Iterative

## When to Use DFS

1. Pathfinding in maze-like problems
2. Topological sorting
3. Detecting cycles in graphs
4. Solving puzzles with only one solution (e.g., sudoku)
5. Generating permutations or combinations

### Recursive DFS is preferred when:
- The graph is known to be shallow
- The solution is known to be far from the root
- The problem naturally fits a recursive formulation
- Simplicity of implementation is prioritized

### Iterative DFS is preferred when:
- The graph might be very deep
- Memory usage is a concern (to avoid stack overflow)
- You need more control over the traversal process

## When Not to Use DFS

1. Finding the shortest path (BFS is usually better)
2. When you need to search level by level
3. When the graph is very deep and recursive DFS might cause stack overflow
4. When you need to find all solutions, not just one (BFS might be more suitable)

# Implementing DFS in Python - Recursive and Iterative

## Recursive DFS Implementation

```python
def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(node)
    print(node, end=' ')  # Process the node
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("Recursive DFS:")
dfs_recursive(graph, 'A')
```

## Iterative DFS Implementation

```python
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node, end=' ')  # Process the node
            
            # Add neighbors to stack in reverse order
            # to match recursive DFS output
            stack.extend(reversed(graph[node]))

# Example usage
print("\nIterative DFS:")
dfs_iterative(graph, 'A')
```

# Scenario Problem: Solving a Maze using DFS

Let's solve a maze problem using iterative DFS. The maze will be represented as a 2D grid where:
- 0 represents a free cell
- 1 represents a wall
- 2 represents the starting point
- 3 represents the exit

Our task is to find a path from the start to the exit.

```python
def solve_maze(maze):
    def is_valid(x, y):
        return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != 1

    def get_neighbors(x, y):
        return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

    start = None
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 2:
                start = (i, j)
                break
        if start:
            break

    stack = [start]
    visited = set()
    parent = {}

    while stack:
        x, y = stack.pop()
        
        if maze[x][y] == 3:  # Exit found
            path = []
            while (x, y) != start:
                path.append((x, y))
                x, y = parent[(x, y)]
            path.append(start)
            return path[::-1]
        
        if (x, y) not in visited:
            visited.add((x, y))
            for nx, ny in get_neighbors(x, y):
                if is_valid(nx, ny) and (nx, ny) not in visited:
                    stack.append((nx, ny))
                    parent[(nx, ny)] = (x, y)
    
    return None  # No path found

# Example maze
maze = [
    [0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 3],
    [2, 1, 0, 0, 0]
]

path = solve_maze(maze)
if path:
    print("Path found:", path)
else:
    print("No path found")

# Visualize the path
def print_maze_with_path(maze, path):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if (i, j) in path:
                print("*", end=" ")
            else:
                print(maze[i][j], end=" ")
        print()

print("\nMaze with path:")
print_maze_with_path(maze, path)
```

This implementation uses iterative DFS to solve the maze. It starts from the starting point (2), explores possible paths using a stack, and backtracks when it hits a wall or a visited cell. When it reaches the exit (3), it reconstructs and returns the path. The visualization shows the path with asterisks (*).

This example demonstrates how DFS can be applied to solve real-world problems like navigating through a maze, showcasing its strength in pathfinding applications.
