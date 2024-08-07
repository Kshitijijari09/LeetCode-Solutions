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
#         current = root
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
        def dfs(root):
            if not root:
                return None
            
            leftTail = dfs(root.left)
            rightTail = dfs(root.right)
            
            if root.left:
                leftTail.right = root.right
                root.right = root.left
                root.left = None
                
            last =  rightTail or leftTail or root 
            
            return last
        
        dfs(root)

        