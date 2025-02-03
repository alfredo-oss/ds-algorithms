"""
Given the root of a binary tree, return the level order traversal of its nodes' values.
(i.e., from left to right, level by level).
input: Optional[TreeNode]
output: List[List[int]]

The premise here is that the nature of the problem doesn't fit recursion. Thus, we will need 
a temporary data structure that will hold the "disconnected" but ordered nodes.

"""
from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        queue = deque()
        if root:
            queue.append(root)
        res = []
        while queue:
            aux = []
            for _ in range(len(queue)): 
                curr = queue.popleft()
                aux.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(aux)
        return res