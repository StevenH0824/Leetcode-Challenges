#2236. Root Equals Sum of Children
# You are given the root of a binary tree that consists of exactly 3 nodes:
# the root, its left child, and its right child.
# Return true if the value of the root is equal to the sum of the values of its two children,
# or false otherwise.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def checkTree(root: [TreeNode]) -> bool:
        return root.val == (root.left.val + root.right.val)

tree1 = TreeNode(10, TreeNode(4), TreeNode(6))
tree2 = TreeNode(5, TreeNode(3), TreeNode(1))



print(checkTree(tree1))
print(checkTree(tree2))

"""
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        return root.val == (root.left.val + root.right.val)
"""