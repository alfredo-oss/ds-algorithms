"""
input: p: Optional[TreeNode], q: Optional[TreeNode]
output: bool
we are given two binary trees p and q, and we have to check if they are or not the same tree.

notes:
------
i think this problem could be approached with any available traversal:
- preorder
- inorder
- postorder
we are allowed to have an external datastructure since O(n) is the 
space complexity defined.
I took a defensive programming approach to solving the problem:
"""
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        res = True
        def dfs(p, q):
            nonlocal res
            if p and not q:
                res = False
                return
            if not p and q:
                res = False
                return
            if not p and not q:
                return
            dfs(p.left, q.left)
            if p.val != q.val:
                res = False
                return
            dfs(p.right, q.right)
        dfs(p, q)
        return res
