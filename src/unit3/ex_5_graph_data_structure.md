# Exercise

These exercises are designed to help you practice working with graph data structures in Python with added visualizations to help you understand the graph structures better.

## File Organization

We'll use the following updated file structure:

```
csf101-python_exercises/
│
└── data_structures/
    ├── arrays.py
    ├── multi_dimensional_arrays.py
    ├── graph_adjacency_matrix.py
    ├── graph_adjacency_list.py
    └── graph_operations.py
```

Before starting, make sure to install the required libraries:

```
pip install numpy networkx matplotlib
```

## Exercise 1: Implementing an Adjacency Matrix with Visualization

File: `data_structures/graph_adjacency_matrix.py`

Update the file `graph_adjacency_matrix.py` in the `data_structures` directory with the following content:

```python
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def visualize_graph(matrix):
    G = nx.Graph()
    for i in range(len(matrix)):
        for j in range(i+1, len(matrix)):
            if matrix[i][j] == 1:
                G.add_edge(i, j)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=16, font_weight='bold')
    plt.title("Graph Visualization")
    plt.show()

# Create an adjacency matrix for an undirected graph with 4 vertices
num_vertices = 4
adj_matrix = np.zeros((num_vertices, num_vertices), dtype=int)
print("Initial adjacency matrix:")
print(adj_matrix)

# Visualize the initial graph
visualize_graph(adj_matrix)

# Function to add an edge
def add_edge(matrix, v1, v2):
    matrix[v1][v2] = 1
    matrix[v2][v1] = 1  # For undirected graph

# Add edges: (0,1), (1,2), (2,3), (3,0)
add_edge(adj_matrix, 0, 1)
add_edge(adj_matrix, 1, 2)
add_edge(adj_matrix, 2, 3)
add_edge(adj_matrix, 3, 0)

print("\nAdjacency matrix after adding edges:")
print(adj_matrix)

# Visualize the graph after adding edges
visualize_graph(adj_matrix)

# Function to check if two vertices are connected
def is_connected(matrix, v1, v2):
    return matrix[v1][v2] == 1

print("\nIs vertex 0 connected to vertex 1?", is_connected(adj_matrix, 0, 1))
print("Is vertex 0 connected to vertex 2?", is_connected(adj_matrix, 0, 2))
```

Expected output:

```
Initial adjacency matrix:
[[0 0 0 0]
 [0 0 0 0]
 [0 0 0 0]
 [0 0 0 0]]

Adjacency matrix after adding edges:
[[0 1 0 1]
 [1 0 1 0]
 [0 1 0 1]
 [1 0 1 0]]

Is vertex 0 connected to vertex 1? True
Is vertex 0 connected to vertex 2? False
```

The script will also display two graph visualizations: one for the initial empty graph and another for the graph after adding edges.

## Exercise 2: Implementing an Adjacency List with Visualization

File: `data_structures/graph_adjacency_list.py`

Update the file `graph_adjacency_list.py` in the `data_structures` directory with the following content:

```python
import networkx as nx
import matplotlib.pyplot as plt

def visualize_graph(graph):
    G = nx.Graph(graph)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=500, font_size=16, font_weight='bold')
    plt.title("Graph Visualization")
    plt.show()

# Create an adjacency list for an undirected graph with 4 vertices
adj_list = {
    0: [],
    1: [],
    2: [],
    3: []
}
print("Initial adjacency list:")
print(adj_list)

# Visualize the initial graph
visualize_graph(adj_list)

# Function to add an edge
def add_edge(graph, v1, v2):
    graph[v1].append(v2)
    graph[v2].append(v1)  # For undirected graph

# Add edges: (0,1), (1,2), (2,3), (3,0)
add_edge(adj_list, 0, 1)
add_edge(adj_list, 1, 2)
add_edge(adj_list, 2, 3)
add_edge(adj_list, 3, 0)

print("\nAdjacency list after adding edges:")
print(adj_list)

# Visualize the graph after adding edges
visualize_graph(adj_list)

# Function to check if two vertices are connected
def is_connected(graph, v1, v2):
    return v2 in graph[v1]

print("\nIs vertex 0 connected to vertex 1?", is_connected(adj_list, 0, 1))
print("Is vertex 0 connected to vertex 2?", is_connected(adj_list, 0, 2))
```

Expected output:

```
Initial adjacency list:
{0: [], 1: [], 2: [], 3: []}

Adjacency list after adding edges:
{0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [2, 0]}

Is vertex 0 connected to vertex 1? True
Is vertex 0 connected to vertex 2? False
```

The script will also display two graph visualizations: one for the initial empty graph and another for the graph after adding edges.

## Exercise 3: Graph Operations with Visualization

File: `data_structures/graph_operations.py`

Update the file `graph_operations.py` in the `data_structures` directory with the following content:

```python
import networkx as nx
import matplotlib.pyplot as plt

def visualize_weighted_graph(graph):
    G = nx.Graph()
    for vertex, neighbors in graph.items():
        for neighbor, weight in neighbors:
            G.add_edge(vertex, neighbor, weight=weight)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightcoral', node_size=500, font_size=16, font_weight='bold')
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title("Weighted Graph Visualization")
    plt.show()

def create_weighted_graph():
    return {
        'A': [('B', 4), ('C', 2)],
        'B': [('A', 4), ('C', 1), ('D', 5)],
        'C': [('A', 2), ('B', 1), ('D', 8), ('E', 10)],
        'D': [('B', 5), ('C', 8), ('E', 2), ('F', 6)],
        'E': [('C', 10), ('D', 2), ('F', 3)],
        'F': [('D', 6), ('E', 3)]
    }

weighted_graph = create_weighted_graph()
print("Weighted graph:")
print(weighted_graph)

# Visualize the weighted graph
visualize_weighted_graph(weighted_graph)

def get_neighbors(graph, vertex):
    return [neighbor for neighbor, _ in graph[vertex]]

print("\nNeighbors of vertex C:", get_neighbors(weighted_graph, 'C'))

def get_edge_weight(graph, v1, v2):
    for neighbor, weight in graph[v1]:
        if neighbor == v2:
            return weight
    return None  # If there's no edge between v1 and v2

print("\nWeight of edge (A, B):", get_edge_weight(weighted_graph, 'A', 'B'))
print("Weight of edge (A, D):", get_edge_weight(weighted_graph, 'A', 'D'))

def total_graph_weight(graph):
    total = 0
    visited = set()
    for vertex in graph:
        for neighbor, weight in graph[vertex]:
            if (vertex, neighbor) not in visited and (neighbor, vertex) not in visited:
                total += weight
                visited.add((vertex, neighbor))
    return total

print("\nTotal weight of the graph:", total_graph_weight(weighted_graph))

def dfs_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for neighbor, _ in graph[start]:
        if neighbor not in path:
            new_paths = dfs_paths(graph, neighbor, end, path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths

print("\nAll paths from A to F:")
all_paths = dfs_paths(weighted_graph, 'A', 'F')
for path in all_paths:
    print(' -> '.join(path))

# Visualize a specific path
def visualize_path(graph, path):
    G = nx.Graph()
    for vertex, neighbors in graph.items():
        for neighbor, weight in neighbors:
            G.add_edge(vertex, neighbor, weight=weight)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightgray', node_size=500, font_size=16, font_weight='bold')

    path_edges = list(zip(path[:-1], path[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)

    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.title(f"Path Visualization: {' -> '.join(path)}")
    plt.show()

# Visualize the first path found
visualize_path(weighted_graph, all_paths[0])
```

Expected output:

```
Weighted graph:
{'A': [('B', 4), ('C', 2)], 'B': [('A', 4), ('C', 1), ('D', 5)], 'C': [('A', 2), ('B', 1), ('D', 8), ('E', 10)], 'D': [('B', 5), ('C', 8), ('E', 2), ('F', 6)], 'E': [('C', 10), ('D', 2), ('F', 3)], 'F': [('D', 6), ('E', 3)]}

Neighbors of vertex C: ['A', 'B', 'D', 'E']

Weight of edge (A, B): 4
Weight of edge (A, D): None

Total weight of the graph: 39

All paths from A to F:
A -> B -> D -> F
A -> B -> D -> E -> F
A -> B -> C -> D -> F
A -> B -> C -> D -> E -> F
A -> B -> C -> E -> F
A -> C -> B -> D -> F
A -> C -> B -> D -> E -> F
A -> C -> D -> F
A -> C -> D -> E -> F
A -> C -> E -> F
```

The script will display three graph visualizations:

1. The initial weighted graph
2. A visualization of the first path found from A to F
3. A visualization of the entire graph with the first path highlighted in red

These visualizations will help students better understand the structure of the graph and how paths are formed within it.

Warning: Make sure you have the required libraries installed (`numpy`, `networkx`, and `matplotlib`) before running these scripts. If you encounter any `ImportError`, you may need to install the missing library using `pip install library_name`.

Note: The graph visualizations may vary slightly each time you run the script due to the random initial positioning of nodes in the spring layout algorithm.

**Congratulations!**

## Final Notes

- These exercises now include visual representations of the graphs, which can greatly aid in understanding the structure and operations of graphs.
- The `networkx` library is a powerful tool for working with graphs in Python. It provides many more algorithms and operations that you can explore as you advance your graph theory knowledge.
- Visualizing graphs can be particularly helpful when dealing with larger, more complex graph structures.
- Remember that while visualizations are helpful, they can become cluttered for very large graphs. In such cases, you might want to visualize only parts of the graph or use different visualization techniques.

Remember to run each file separately to see the output and visualizations of your exercises. You can do this by navigating to the appropriate directory in your terminal and running `python filename.py` (e.g., `python graph_adjacency_matrix.py`).
