class Treenode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Insert a new node and return the root of the BST
def insert(root, val):
    if not root:
        return Treenode(val)
    
    if val > root.val:
        root.right = insert(root.right, val)
    elif val < root.val:
        root.left = insert(root.left, val)
    # Finally the subtree needs to be returned
    return root

# Return the minium value of the BST
def minValueNode(root):
    curr = root
    while curr and curr.left:
        curr = curr.left
    return curr