"""
Given the root of a binary tree, return its depth.
The depth of a binary tree is defined as the number of nodes along the 
longest path from the root node down to the farthest leaf node.

notes:
------
the longest path is either the left or right path.
|
 --> which is a recursive call 
to return the number of nodes I could create an auxiliary variable 
or just do 1 + dfs(node)
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(1 + self.maxDepth(root.left), 1 + self.maxDepth(root.right))