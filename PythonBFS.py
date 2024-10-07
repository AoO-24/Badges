from collections import deque

# Define BFS function
def BFS(graph, root):
  visited = set() # Set to keep track of visited nodes
  queue = deque() # A queue to add nodes for visiting
  visited_order = [] # List to keep visited nodes in order they are visited
  queue.append(root) # start with the root node

  while queue: # While there are nodes to visit.
    node = queue.popleft() # Visit the first node in the queue.
    visited_order.append(node) # Track the order by adding it to the list of visited nodes.
    visited.add(node) # Mark the node as visited. (More efficient way to solve the question.)

    for child in graph:
      if child not in visited:
        queue.append(child)

    return visited

# Define the adjacency list of our graph
graph = {
    '1': ['2', '3', '4'],
    '2': ['1', '5', '6'],
    '3': ['1', '7', '8'],
    '4': ['1', '9', '10'],
    '5': ['2'],
    '6': ['2', '11'],
    '7': ['3'],
    '8': ['3'],
    '9': ['4'],
    '10': ['4'],
    '11': ['6']
}

# Call the BFS function
print(BFS(graph, '1'))
