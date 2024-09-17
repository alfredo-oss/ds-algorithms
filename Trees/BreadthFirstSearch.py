from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left

class Solution:
    def bfs(self, root: Optional[TreeNode]):
        queue = deque()

        if root:
            queue.append(root)

        level = 0
        while len(queue) > 0:
            print("level: ", level)
            for i in range(len(queue)):
                curr = queue.popleft()
                print(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            level += 1
                
