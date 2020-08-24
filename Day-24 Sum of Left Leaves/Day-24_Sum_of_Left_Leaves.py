'''
    
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.s=0
        def traversal(root):
            if not root:
                return
            traversal(root.right)
            if root.left and root.left.left==None and root.left.right==None:
                self.s=self.s+root.left.val
                return
            traversal(root.left)
            
        traversal(root)
        return self.s