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
        queue.append(root)

        while queue:
            rightSideNode = None
            qLen = len(queue)

            for i in range(qLen):
                node = queue.popleft()
                if node:
                    rightSideNode = node
                    queue.append(node.left)
                    queue.append(node.right)

            if rightSideNode:
                res.append(rightSideNode.val)
        
        return res