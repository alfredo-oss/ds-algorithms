from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.right=right
        self.left=left

class Solution:
    def preOrderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []

        def preorder(root):
            if not root:
                return
            
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)

        preorder(root)
        return res
