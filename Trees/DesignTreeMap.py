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

        while True:

            if key < curr.key:
                curr = curr.left

            elif key > curr.key:
                curr = curr.right

            else:
                return curr.val
            
        return -1
        