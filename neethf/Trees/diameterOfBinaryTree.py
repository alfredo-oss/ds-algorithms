"""
The diameter of a binary tree is defined as the length of the longest path between
any two nodes within the tree. The path does not necessarily have to pass through 
the root.

The length of the path between two nodes in a binary tree is the number of edges
between the nodes.

notes:
-----
the maximum distance between 2 nodes can be defined as:
the maximum depth of the left side + max depth of right side.
but the catch here is that only roots with 2 nodes can have this consideration.

the question here is: how do we measure the distance between two nodes that are
completely separated. we would just sum up their depths...
"""
