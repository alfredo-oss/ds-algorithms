from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, right=None, left=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def rightSideView(self, root:Optional[TreeNode]) -> List[int]:

        res = []
        queue = deque()

        if not root:
            return res
        
        queue.append(root)
        res.append(root.val)
        level = 0

        while len(queue) > 0:
            print(f"Traversing Level: {level}")
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr.right:
                    queue.append(curr.right)
                    res.append(curr.right.val)
            level += 1
        return res