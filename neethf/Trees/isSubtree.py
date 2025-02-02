"""
input: root: Optional[TreeNode], subRoot: Optional[TreeNode]
output: bool

Given the roots of two binary trees, return true if there is a subtree of 
root with the same structure and node values of subRoot and false otherwise.

notes:
-------
** the catch here is that we cant start at the same root and start comparing values 
right away, like we did in the sameTree problem.
** initially, we do not know wether the subtree is on the left or right sub-tree.
** using an auxiliary array to compare the inorder-traversal elements would not 
   be correct.
solution:
--------
I need to define a dfs to possibly traverse the whole "root" tree and recursively check if each node
is the root of an "equal" subtree
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        res = False
        def dfs(root):
            nonlocal res
            nonlocal subRoot
            if not root:
                return
            if not self.sameTree(root, subRoot):
                res = True
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return res
    
    def sameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        res = True
        def dfs(p,q):
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