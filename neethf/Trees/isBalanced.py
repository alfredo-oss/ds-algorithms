"""
Given the root of a binary tree, determine if it is height balanced:
A tree is balanced if the height comparison between every left and right
node does not differ more than one unit.

notes:
-----
i could recursively traverse both left and right nodes of the tree,
returning the left and right height, if the difference between them
is greater than one unit, then we can return false or true.
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def isBalanced(self, root: Optional[TreeNode]):
        comp = True
        def dfs(root):
            nonlocal comp
            if not root:
                return 1
            left = self.isBalanced(root.left)
            right = self.isBalanced(root.right)
            res = abs(left - right)
            print(res)
            if res > 1:
                comp = False
            return 1 + max(left, right)
        dfs(root)
        return comp
    