# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        # Set the first depth to 0
        queue = [(root, 0)]
        result = [[]]

        while len(queue) > 0:
            node, depth = queue.pop(0)
            # Dynamically enlarge the result list
            if depth > len(result) - 1:
                result.append([])
            result[depth].append(node.val)

            depth += 1
            if node.left:
                queue.append((node.left, depth))
            if node.right:
                queue.append((node.right, depth))

        return result









            












