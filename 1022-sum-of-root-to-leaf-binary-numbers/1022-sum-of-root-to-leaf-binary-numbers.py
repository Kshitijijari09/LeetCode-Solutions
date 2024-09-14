# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self,node, sum_tree):
        if not node:
            return 0
        sum_tree = 2 * sum_tree + node.val
        if not node.left and not node.right:
            return sum_tree
        return self.preorder(node.left, sum_tree) + self.preorder(node.right, sum_tree)
    
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        return self.preorder(root,0)
    
    