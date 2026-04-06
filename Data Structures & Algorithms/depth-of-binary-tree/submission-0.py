# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Order doesn't matter here, will use DFS
        depth, left_depth, right_depth = 0, 0, 0
        if not root:
            return depth
        
        depth += 1
        if root.left:
            left_depth = depth + self.maxDepth(root.left)
        if root.right:
            right_depth = depth + self.maxDepth(root.right)
        return max(depth, left_depth, right_depth)
