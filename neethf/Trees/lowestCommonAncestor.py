"""
input: p: Optional[TreeNode] q: Optional[TreeNode]
output: LCA: Optional[TreeNode]

notes:
-----
lca: the lowest common ancestor between two nodes p and q is the lowest node in a tree T such that both p and q as descendants.
The ancestor is allowed to be a descendant of itself.
If a think of a typical traversal, I will always be calling the parent nodes and then do something with the values.

# Now, if I did this with just one value I would check if either root.left or root.right has the value im looking for
if so, return the value of root.

# the simplest case would be where p and q are childs of the first node:
# the lca will be the ancestor of the first value we find  
  
  p, q = 3, 8            
              [5]
             /   \
          [3]     [8]
         /  \     /  \
       [1]  [4] [7]   [9]

[KEY INSIGHT]: The key insight to this problem is the fact that we are facing a Binary Tree, thus, a Tree with the sorted property.
The sorted property states the following:
Given a node root:  [root]
                    /    \
its left node:  [left]  [right] : its right node,   
has a smaller                     has to be greater
value

so: 
   [left 
   movement] if p and q are less than the root we are now we 
             have to move to keep traversing to the left
   [right
   movement] if p and q are greater than the root we are now
             we have to move to keep traversing to the right
  [else] we know we have to split our journey, thus, we return
         the current root. 

  restrictions:
  -------------
  [*] the problem states that p, q will both exist in the tree, so
      its not necessary to handle the edge case.
  
  learnings:
  ----------
  [*] using two consecutive "if" statements will evaluate no matter
      what, in the same iteration.
  [*] "elif" handles this problem. so if you dont want to check a condition
      given that the first one evaluated to true, use "elif".
"""