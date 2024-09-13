from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, right=None, left=None):
        self.val = None
        self.right = right
        self.left = left

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k:int) -> int:
        res = []
        stack = []
        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        
        return res[k-1]