# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    val = 0
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            if not node:
                return 0

            if node.val < low:
                dfs(node.right)
                return 0
            if node.val > high:
                dfs(node.left)
                return 0
            
            self.val += node.val

            if low <= node.val <= high:
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        return self.val