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
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, left + right)
            return 1 + max(left, right)
        dfs(root)
        return res