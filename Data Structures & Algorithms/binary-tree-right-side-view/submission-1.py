# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        result = []
        levels = []
        queue = [(root, 0)]

        while len(queue) > 0:
            node, depth = queue.pop(0)
            if len(levels) - 1 < depth:
                levels.append([])
            levels[depth].append(node.val)
            depth += 1

            if node.left:
                queue.append((node.left, depth))
            if node.right:
                queue.append((node.right, depth))
        
        print(levels)
        for level in levels:
            result.append(level[-1])
        
        return result






