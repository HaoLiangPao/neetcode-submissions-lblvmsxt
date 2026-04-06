# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    count = 0

    def goodNodes(self, root: TreeNode) -> int:
        # When traversing the tree, we shall pass down a max value
        if not root:
            return 0

        def dfs(node: TreeNode, maxVal: int) -> None:
            if not node:
                return None

            if node.val >= maxVal:
                self.count += 1
                maxVal = node.val
            
            left = dfs(node.left, maxVal)
            right = dfs(node.right, maxVal)

        dfs(root, root.val)
        return self.count









