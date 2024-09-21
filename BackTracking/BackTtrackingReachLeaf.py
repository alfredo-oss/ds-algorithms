from typing import Optional, List

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def  canReachLeaf(self, root: Optional[TreeNode]) -> bool:
        if not root or root.val == 0:
            return False
        
        if not root.left and not root.right:
            return True
        if self.canReachLeaf(root.left):
            return True
        if self.canReachLeaf(root.right):
            return True
        
        return False
    
    def leafPath(self, root: Optional[TreeNode], path: List[int]) -> List[int]:
        if not root or root.val == 0:
            return False
        
        path.append(root.val)

        if not root.left and not root.right:
            return True
        if self.leafPath(root.left):
            return True
        if self.leafPath(root.right):
            return True
        path.pop()
        return False