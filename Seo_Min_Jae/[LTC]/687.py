# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node, res):
            if not node:
                return 0
            
            left = dfs(node.left, res)
            right = dfs(node.right, res)

            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0
            
            res[0] = max(res[0], left + right)
            return max(left, right)
        
        res = [0]
        dfs(root, res)
        return res[0]