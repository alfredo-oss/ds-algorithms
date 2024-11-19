"""
Clone Graph:
Each node in an undirected graph contains:
    - an integer value
    - a list of its neighbors
* nodes are numbered from 1 to n, where n is the number of nodes on the graph.
* the index of each unique node within the adjacency list is the same
  as the node's value. (1-indexed).
* the input node will always be the first node in the graph and have 1 as value.
---
The input will always be an adjacency list of type:
input = [[2],[1,3],[2]] # which if its mapped to a key each index needs to be incremented by 1, since it its 1-indexed.
output = a deep copy of the input graph.

The input is a list of nodes. With the keys in hinsight as indexes.
I dont get why I would create an underlying structure and not return the same input
-> You cant return a copy
-> Nodes are not iterable by default
-> They have no len() attribute.
"""
"""
** The trick here is: How to access the node structure
"""
from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node) if node else None    