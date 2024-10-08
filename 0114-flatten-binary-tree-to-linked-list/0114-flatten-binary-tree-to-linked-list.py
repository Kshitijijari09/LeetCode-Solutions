# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(node):
            if not node:
                return None
            
            lefttail = dfs(node.left)
            righttail = dfs(node.right)
            
            if node.left:
                lefttail.right = node.right
                node.right = node.left
                node.left = None
            
            flatten = righttail or lefttail or node
            
            return flatten
        
        dfs(root)
        current = root
#         while current:
#             if current.left:
#                 # Find the rightmost node of the left subtree
#                 rightmost = current.left
#                 while rightmost.right:
#                     rightmost = rightmost.right

#                 # Move the right subtree to the rightmost node of the left subtree
#                 rightmost.right = current.right
#                 current.right = current.left
#                 current.left = None

#             # Move to the next node
#             current = current.right