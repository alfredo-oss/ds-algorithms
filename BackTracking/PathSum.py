from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        targetSum -= root.val

        if not root.left and not root.right and targetSum == 0:
            return True

        if self.hasPathSum(root.left):
            return True
        if self.hasPathSum(root.right):
            return True
        targetSum += root.val
        return False 