# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # At every node, we check the sum of left and right node length (as diameter needs to be always connected)
        self.res = 0

        def dfs(curr: Optional[TreeNode]) -> int:
            if not curr:
                return 0
            
            left = dfs(curr.left)
            right = dfs(curr.right)

            self.res = max(self.res, left + right)
            return 1 + max(left, right)

        depth = dfs(root)
        print(f"Depth is {depth}, res is {self.res}")
        return max(depth-1, self.res)

            
