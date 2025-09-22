# BreadthFirst Search

# Concept

Breadth-First Search (BFS) is a fundamental graph traversal algorithm used in computer science and artificial intelligence. Unlike Depth-First Search (DFS), which explores as far as possible along each branch before backtracking, BFS explores all the neighbor nodes at the present depth prior to moving on to the nodes at the next depth level.

The key characteristic of BFS is its "breadth-first" nature: it visits all the vertices at the same level before moving to the vertices at the next level. This behavior is analogous to how a ripple spreads out in a pond, reaching all points at a certain distance before moving further.

<iframe width="560" height="315" src="https://www.youtube.com/embed/HZ5YTanv5QE?si=BEG28xQHfQOfGbMW" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

# How BFS Works - Iterative

BFS is typically implemented iteratively using a queue data structure. Here's how it works:

1. Start at a chosen node (often called the root in tree structures).
2. Mark the current node as visited and enqueue it.
3. While the queue is not empty:
   a. Dequeue a node from the front of the queue.
   b. Explore all unvisited neighbors of this node:
      - Mark each neighbor as visited.
      - Enqueue each neighbor.
4. Repeat step 3 until the queue is empty.

This process ensures that we explore all nodes at a given depth before moving to the next depth level.

**Note:** While it's possible to implement BFS recursively, it's not common or practical due to the nature of the algorithm. The iterative implementation using a queue is the standard approach.

# Time / Space Complexity

## Time Complexity
- O(V + E) for an adjacency list representation
- O(V^2) for an adjacency matrix representation

Where V is the number of vertices and E is the number of edges in the graph.

This is because each vertex and edge will be explored once.

## Space Complexity
- O(V) where V is the number of vertices

The space is used by the queue data structure. In the worst case, the queue might need to store all vertices of the graph.

# When to Use & When Not to Use BFS

## When to Use BFS

1. Finding the shortest path in an unweighted graph
2. Level-order traversal of a tree
3. Finding all nodes within one connected component
4. Testing if a graph is bipartite
5. Finding the shortest path between two nodes
6. Web crawling
7. Social networking features (e.g., finding all friends within a certain degree of connection)

## When Not to Use BFS

1. When memory is a constraint (as it may need to store many nodes)
2. When exploring deeper paths in a graph is prioritized
3. When the solution is likely to be far from the root (DFS might be faster)
4. When working with infinite graphs or trees (as BFS expands in all directions)

# Implementing BFS in Python

Here's a Python implementation of BFS:

```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')  # Process the node

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("BFS traversal:")
bfs(graph, 'A')
```

# Example Problem: Shortest Path in a Maze

Let's solve a maze problem using BFS to find the shortest path. The maze will be represented as a 2D grid where:
- 0 represents a free cell
- 1 represents a wall
- 2 represents the starting point
- 3 represents the exit

Our task is to find the shortest path from the start to the exit.

```python
from collections import deque

def solve_maze_bfs(maze):
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

    queue = deque([start])
    visited = set([start])
    parent = {}

    while queue:
        x, y = queue.popleft()
        
        if maze[x][y] == 3:  # Exit found
            path = []
            while (x, y) != start:
                path.append((x, y))
                x, y = parent[(x, y)]
            path.append(start)
            return path[::-1]
        
        for nx, ny in get_neighbors(x, y):
            if is_valid(nx, ny) and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny))
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

path = solve_maze_bfs(maze)
if path:
    print("Shortest path found:", path)
    print("Path length:", len(path) - 1)  # -1 because we don't count the starting position
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

print("\nMaze with shortest path:")
print_maze_with_path(maze, path)
```

This implementation uses BFS to solve the maze. It starts from the starting point (2), explores possible paths using a queue, and keeps track of the parent of each cell. When it reaches the exit (3), it reconstructs and returns the shortest path. The visualization shows the path with asterisks (*).

This example demonstrates how BFS can be applied to find the shortest path in a maze, showcasing its strength in finding optimal solutions in unweighted graphs.
