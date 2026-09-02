# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        return self.nDepth(root, 0)
    def nDepth(self, root, n):
        if not root:
            return n
        return max(self.nDepth(root.left, n + 1), self.nDepth(root.right, n + 1))