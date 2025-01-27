from typing import List, Optional

class TreeNode:
    def __init__(self, key:int, val:int):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        newNode = TreeNode(key, val)
        
        if self.root == None:
            self.root = newNode
            return
        
        curr = self.root
        while True:
            if key < curr.key:
                if not curr.left:
                    curr.left = newNode
                    return
                curr = curr.left
                            
            elif key > curr.key:
                if not curr.right:
                    curr.right = newNode
                    return
                curr = curr.right
                
            else:
                curr.val = val
                return
    
    def get(self, key: int) -> int:
        curr = self.root

        while curr:

            if key < curr.key:
                curr = curr.left

            elif key > curr.key:
                curr = curr.right

            else:
                return curr.val
            
        return -1
    
    def getMin(self) -> int:
        current = self.findMin(self.root)
        return current.val if current else -1
        
    def findMin(self, node: TreeNode) -> TreeNode:
        while node and node.left:
            node = node.left
        return node
        
    def getMax(self) -> int:
        curr = self.root

        while curr and curr.right:
            curr = curr.right
        return curr.val if curr else -1
        
    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)

    def removeHelper(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
         
        if key < root.key:
            root.left = self.removeHelper(root.left, key)
        elif key > root.key:
            root.right = self.removeHelper(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                minNode = self.findMin(root.right)
                root.key = minNode.key
                root.val = minNode.val
                root.right = self.removeHelper(root.right, minNode.key)

        return root

    def getInorderKeys(self) -> List[int]:

        res = []

        def inorder(root):
            if not root:
                return
            
            inorder(root.left)
            res.append(root.key)
            inorder(root.right)
        inorder(self.root)
        return res