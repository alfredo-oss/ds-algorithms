from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k:int) -> int:
        res = []

        def inorder(root: Optional[TreeNode]) -> List[int]:
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

            return res
        
        return res[k-1]