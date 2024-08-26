# Exercise

These exercises are designed to help you practice working with tree data structures in Python, focusing on binary trees and binary search trees. Follow each step carefully and try to predict the output before running the code.

## File Organization

To keep your work organized, we'll use the following file structure:

```
csf101-python_exercises/
│
├── data_structures/
│   ├── arrays.py
│   ├── multi_dimensional_arrays.py
│   ├── binary_tree.py
│   └── binary_search_tree.py
│
└── visualizations/
    ├── tree_viz.py
    └── traversal_viz.py
```

Navigate to your existing `csf101-python_exercises/data_structures/` directory. We'll add new files here and create a new `visualizations` directory.

## Exercise 1: Implementing a Binary Tree

File: `data_structures/binary_tree.py`

Create a new file called `binary_tree.py` in the `data_structures` directory and complete the following exercises in this file.

1. Implement a function to create a binary tree node.

   ```python
   def create_node(value):
       return {"value": value, "left": None, "right": None}

   # Test the function
   root = create_node(1)
   print(root)
   ```

   Expected output: `{'value': 1, 'left': None, 'right': None}`

2. Create a simple binary tree with a root and two children.

   ```python
   root = create_node(1)
   root["left"] = create_node(2)
   root["right"] = create_node(3)

   print(f"Root: {root['value']}")
   print(f"Left child: {root['left']['value']}")
   print(f"Right child: {root['right']['value']}")
   ```

   Expected output:

   ```
   Root: 1
   Left child: 2
   Right child: 3
   ```

3. Implement a function to perform an in-order traversal of the binary tree.

   ```python
   def inorder_traversal(root):
       result = []
       if root:
           result.extend(inorder_traversal(root["left"]))
           result.append(root["value"])
           result.extend(inorder_traversal(root["right"]))
       return result

   # Test the function
   traversal_result = inorder_traversal(root)
   print("In-order traversal:", traversal_result)
   ```

   Expected output: `In-order traversal: [2, 1, 3]`

   Warning: Make sure your recursive function has a base case to avoid infinite recursion!

## Exercise 2: Implementing a Binary Search Tree

File: `data_structures/binary_search_tree.py`

Create a new file called `binary_search_tree.py` in the `data_structures` directory and complete the following exercises in this file.

4. Implement a function to insert a value into a BST.

   ```python
   def insert(root, value):
       if root is None:
           return create_node(value)
       if value < root["value"]:
           root["left"] = insert(root["left"], value)
       else:
           root["right"] = insert(root["right"], value)
       return root

   # Test the function
   bst_root = None
   for value in [5, 3, 7, 1, 9]:
       bst_root = insert(bst_root, value)

   print("In-order traversal of BST:", inorder_traversal(bst_root))
   ```

   Expected output: `In-order traversal of BST: [1, 3, 5, 7, 9]`

5. Implement a function to search for a value in the BST.

   ```python
   def search(root, value):
       if root is None or root["value"] == value:
           return root
       if value < root["value"]:
           return search(root["left"], value)
       return search(root["right"], value)

   # Test the function
   print("Search for 3:", search(bst_root, 3))
   print("Search for 6:", search(bst_root, 6))
   ```

   Expected output:

   ```
   Search for 3: {'value': 3, 'left': {'value': 1, 'left': None, 'right': None}, 'right': None}
   Search for 6: None
   ```

6. Implement a function to find the minimum value in the BST.

   ```python
   def find_min(root):
       if root is None:
           return None
       while root["left"]:
           root = root["left"]
       return root["value"]

   # Test the function
   print("Minimum value in BST:", find_min(bst_root))
   ```

   Expected output: `Minimum value in BST: 1`

   Warning: Be careful with empty trees! Always check if the root is None.

## Exercise 3: Tree Visualization

File: `visualizations/tree_viz.py`

Create a new file called `tree_viz.py` in the `visualizations` directory and complete the following exercises in this file.

7. Implement a function to visualize a binary tree using the `graphviz` library.

   ```python
   from graphviz import Digraph

   def visualize_tree(root):
       dot = Digraph()
       dot.node(str(id(root)), str(root["value"]))

       def add_nodes_edges(node):
           if node["left"]:
               dot.node(str(id(node["left"])), str(node["left"]["value"]))
               dot.edge(str(id(node)), str(id(node["left"])))
               add_nodes_edges(node["left"])
           if node["right"]:
               dot.node(str(id(node["right"])), str(node["right"]["value"]))
               dot.edge(str(id(node)), str(id(node["right"])))
               add_nodes_edges(node["right"])

       add_nodes_edges(root)
       return dot

   # Test the function (use the BST from Exercise 2)
   tree_viz = visualize_tree(bst_root)
   tree_viz.render("bst_visualization", format="png", cleanup=True)
   print("BST visualization saved as 'bst_visualization.png'")
   ```

   Expected output: `BST visualization saved as 'bst_visualization.png'`

   Note: Make sure you have the `graphviz` library installed (`pip install graphviz`).

## Exercise 4: Traversal Visualization

File: `visualizations/traversal_viz.py`

Create a new file called `traversal_viz.py` in the `visualizations` directory and complete the following exercises in this file.

8. Implement a function to visualize tree traversals using `networkx` and `matplotlib`.

   ```python
   import networkx as nx
   import matplotlib.pyplot as plt

   def create_graph(root):
       G = nx.DiGraph()

       def add_edges(node):
           if node["left"]:
               G.add_edge(node["value"], node["left"]["value"])
               add_edges(node["left"])
           if node["right"]:
               G.add_edge(node["value"], node["right"]["value"])
               add_edges(node["right"])

       add_edges(root)
       return G

   def visualize_traversal(root, traversal_func, title):
       G = create_graph(root)
       pos = nx.spring_layout(G)

       plt.figure(figsize=(10, 6))
       nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, arrows=True)

       traversal = traversal_func(root)
       edge_colors = ['r' if (traversal[i], traversal[i+1]) in G.edges() or (traversal[i+1], traversal[i]) in G.edges()
                      else 'k' for i in range(len(traversal)-1)]

       nx.draw_networkx_edges(G, pos, edgelist=list(G.edges()), edge_color=edge_colors, arrows=True)

       plt.title(title)
       plt.axis('off')
       plt.tight_layout()
       plt.savefig(f"{title.lower().replace(' ', '_')}.png")
       print(f"Traversal visualization saved as '{title.lower().replace(' ', '_')}.png'")

   # Test the function (use the BST and inorder_traversal from previous exercises)
   visualize_traversal(bst_root, inorder_traversal, "In-order Traversal")
   ```

   Expected output: `Traversal visualization saved as 'in_order_traversal.png'`

   Note: Make sure you have the `networkx` and `matplotlib` libraries installed (`pip install networkx matplotlib`).

## Exercise 5: Advanced BST Operations

File: `data_structures/binary_search_tree.py`

Add the following exercises to your existing `binary_search_tree.py` file.

9. Implement a function to delete a node from the BST.

   ```python
   def min_value_node(node):
       current = node
       while current["left"]:
           current = current["left"]
       return current

   def delete(root, value):
       if root is None:
           return root
       if value < root["value"]:
           root["left"] = delete(root["left"], value)
       elif value > root["value"]:
           root["right"] = delete(root["right"], value)
       else:
           if root["left"] is None:
               return root["right"]
           elif root["right"] is None:
               return root["left"]
           temp = min_value_node(root["right"])
           root["value"] = temp["value"]
           root["right"] = delete(root["right"], temp["value"])
       return root

   # Test the function
   print("BST before deletion:", inorder_traversal(bst_root))
   bst_root = delete(bst_root, 3)
   print("BST after deleting 3:", inorder_traversal(bst_root))
   ```

   Expected output:

   ```
   BST before deletion: [1, 3, 5, 7, 9]
   BST after deleting 3: [1, 5, 7, 9]
   ```

   Warning: Deleting nodes can be tricky! Make sure to handle all cases (leaf nodes, nodes with one child, and nodes with two children) correctly.

10. Implement a function to find the height of the BST.

    ```python
    def tree_height(root):
        if root is None:
            return -1
        left_height = tree_height(root["left"])
        right_height = tree_height(root["right"])
        return max(left_height, right_height) + 1

    # Test the function
    print("Height of the BST:", tree_height(bst_root))
    ```

    Expected output: `Height of the BST: 3`

    Note: The height of an empty tree is typically defined as -1, and the height of a tree with only a root node is 0.

**Congratulations!** You've completed the exercises on tree data structures.

## Final Notes

- These exercises cover the basics of binary trees and binary search trees. As you progress, you can explore more advanced topics like AVL trees, Red-Black trees, or B-trees.
- Remember to visualize your trees often. It helps in understanding the structure and verifying if your operations are correct.
- Always consider edge cases, such as empty trees or trees with only one node, when implementing tree operations.

To run these exercises, navigate to the appropriate directory in your terminal and run `python filename.py` (e.g., `python binary_tree.py`). For visualization exercises, make sure you have the required libraries installed.
