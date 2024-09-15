# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        dummy = TreeNode()
        cursor = dummy
        
        def inorder(node):
            nonlocal cursor
            if not node:
                return

            inorder(node.left)
            cursor.right = TreeNode(node.val)
            cursor = cursor.right 

            inorder(node.right)
        
        inorder(root)
        
        return dummy.right
        
      