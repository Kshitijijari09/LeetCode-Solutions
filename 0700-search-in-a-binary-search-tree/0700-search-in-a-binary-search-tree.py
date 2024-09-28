# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
         # First check if root is None
        if not root:
            return None
        
        # If the current node has the desired value, return it
        if root.val == val:
            return root
        
        # If the value is greater, search in the right subtree
        if root.val < val:
            return self.searchBST(root.right, val)
        
        # Otherwise, search in the left subtree
        return self.searchBST(root.left, val)