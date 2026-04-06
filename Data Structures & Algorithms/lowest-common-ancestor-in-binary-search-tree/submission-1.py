# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # No need to iterate through the whole tree because it is a BST, just compare the value of the root node and the two nodes we are intertested in

        # No need to check the Null as they should exist due to constraints
        queue = [root]

        while len(queue) > 0:
            node = queue.pop(0)
            # print(f"Curr node is: {node.val}")

            # p,q are both at right
            if p.val > node.val and q.val > node.val:
                queue.append(node.right)
            
            # p,q are both at left
            if p.val < node.val and q.val < node.val:
                queue.append(node.left)
            
            if q.val <= node.val <= p.val or p.val <= node.val <= q.val:
                return node

            
