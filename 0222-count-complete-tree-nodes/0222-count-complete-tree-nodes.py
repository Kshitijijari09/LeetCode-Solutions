# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root:
            counter = 1
        else:
            return 0
            
        def dfs(node):
            nonlocal counter
            if not node:
                return 0
            counter += 1
            
            return dfs(node.left) or dfs(node.right)
        dfs(root.left)
        dfs(root.right)
        return counter