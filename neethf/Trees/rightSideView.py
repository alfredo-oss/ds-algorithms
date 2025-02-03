"""
You are given the root of a binary tree. Return only the of the nodes that are
visible from the right side of the tree, ordered from top to bottom.

notes:
------
this is not as easy as just adding the right nodes, what if a tree only has 
left nodes. those can be viewed from the right side.
at the end what i want is not to pop in the order that we defined: "FIFO", I will want to 
pop in a LIFO order because the last added node in the level is the one that is going to 
be visible from the right side
"""
from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root:Optional[TreeNode]) -> list[int]:
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
            res.append(aux[-1])
        return res