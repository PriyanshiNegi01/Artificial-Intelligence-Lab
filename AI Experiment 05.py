#!/usr/bin/env python
# coding: utf-8

# # Experiment 04: BFS and DFS
# 
# ## Aim: 
# To implement Python code for BFS and DFS traversal of a graph.
# 
# ## Program:

# In[1]:


# BFS:
graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

visited = [] # List for visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node): #function for BFS
  visited.append(node)
  queue.append(node)

  while queue:          # Creating loop to visit each node
    m = queue.pop(0)
    print (m, end = " ")

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code
print("Breadth-First Search")
bfs(visited, graph, 'A')    # function calling


# ## Algorithm (BFS):
# 
# 1. Start with an empty list 'visited' to keep track of visited nodes and an empty queue 'queue' for BFS traversal.
# 
# 2. Enqueue the starting node (root node) into the 'queue' and mark it as visited by adding it to the 'visited' list.
# 
# 3. While the 'queue' is not empty:
# 
# - Dequeue a node 'current_node' from the front of the queue.
# - Print or process 'current_node'.
# - Enqueue all unvisited neighbors of 'current_node' into the 'queue', and mark them as visited by adding them to the 'visited' list.
# 
# 4. Repeat step 3 until the queue becomes empty.
# 
# 5. When the BFS traversal is complete (the queue is empty), the algorithm has visited all reachable nodes in the graph.
# 
# The time complexity of BFS is O(V + E), where V is the number of vertices (nodes) and E is the number of edges in the graph.
# 
# The space complexity of BFS is O(V), where V is the number of vertices. This space is primarily used for the visited list and the queue.

# In[2]:


# DFS
# Using a Python dictionary to act as an adjacency list
graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

visited = set() # Set to keep track of visited nodes of graph.

def dfs(visited, graph, node):  #function for dfs
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
print("Following is the Depth-First Search")
dfs(visited, graph, 'A')


# ## Algorithm (DFS):
# 
# 1. Initialize an empty set visited to keep track of visited nodes.
# 
# 2. Define a function dfs(visited, graph, node) to perform DFS traversal:
# 
# - If the current node node is not visited:
#     - Mark the current node node as visited by adding it to the visited set.
#     - Print or process the current node.
#     - Recursively call dfs() on all unvisited neighbors of the current node node.
# 
# 3. Call the dfs() function with the starting node to initiate the DFS traversal.
# 
# The time complexity of DFS is O(V + E), where V is the number of vertices (nodes) and E is the number of edges in the graph. This is because each vertex and each edge will be visited once during the traversal.
# 
# The space complexity of DFS is O(V), where V is the number of vertices. This space is primarily used for the visited set, which keeps track of visited nodes. Additionally, the recursive calls of the DFS function consume space on the call stack proportional to the depth of the recursion, which is bounded by the number of vertices in the graph.
