"""
Binary Search Trees make the assumption of having a roughly balanced tree to be executed in a O(log n).
"""
class Treenode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def search(root: Treenode, target: int) -> bool:
    if not root:
        return False
    
    if target > root.val:
        return search(root.right, target)
    
    elif target < root.val:
        return search(root.left, target)
    
    else:
        return True
    
