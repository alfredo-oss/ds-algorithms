from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root:Optional[TreeNode]) -> List[List[int]]:
        res = []
        subls = []
        queue = deque()

        if not root:
            return None
        
        queue.append(root)
        subls.append(root.val)
        res.append(subls)
        level = 0

        while len(queue) > 0:
            print(f"Traversing Level :{level}")
            subls = []
            for i in range(len(queue)): # The length of the queue is not modified on the loop, the loop is executed based on the value its initially given. It doesnt matter if its modified afterwise.
                curr = queue.popleft() # We apply first-in/first-out processing
                if curr.left:
                    queue.append(curr.left)
                    subls.append(curr.left.val)
                if curr.right:
                    queue.append(curr.right)
                    subls.append(curr.right.val)
            level += 1
