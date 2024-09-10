from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key:int) -> Optional[TreeNode]:

        if root.val < key:
            root.right = self.deleteNode(root.right, key)

        elif root.val > key:
            root.left = self.deleteNode(root.left, key)

        else:
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            else:
                minValue = self.findMin(root)
                root.val = minValue
                root = self.deleteNode(root, minValue)

    def findMin(self, root: Optional[TreeNode]) -> int:
        
        curr =  root
        while curr and curr.left:
            curr =  curr.left
        return curr

