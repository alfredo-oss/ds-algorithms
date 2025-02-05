"""
within a binary tree (which has no sorted property), a node "x" is considered "good" if the path from the root of the tree
to the node "x" contains no nodes with a value greater than the value of node "x".

given the root of a binary tree "root", return the number of good nodes within the tree.

notes:
-----
This is a level order traversal because its what makes the most sense if we are exploring the
childs of each level.
It would look something like this:
"""
from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque()
        queue.append(root)
        count = 1
        max_left, max_right = root.val, root.val
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur.left:
                    if cur.left.val >= max_left:
                        count += 1
                    max_left = max(max_left, cur.left.val)
                    queue.append(cur.left)
                if cur.right:
                    if cur.right.val >= max_right:
                        count += 1
                    max_right = max(max_right, cur.right.val)
                    queue.append(cur.right)
        return count