# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # We can create a queue of visit order, and we go from left, right of that queue on both nodes
        def generate_full_order(root):
            
            if not root:
                return []

            queue = [root]
            order = [root.val]

            # It is introduced to reserve node structure
            NULL_REPLACEMENT = -111

            while len(queue) > 0:
                curr = queue.pop(0)
                if curr.left:
                    queue.append(curr.left)
                    order.append(curr.left.val)
                else:
                    order.append(NULL_REPLACEMENT)

                if curr.right:
                    queue.append(curr.right)
                    order.append(curr.right.val)
                else:
                    order.append(NULL_REPLACEMENT)
            
            return order
        
        order_p = generate_full_order(p)
        order_q = generate_full_order(q)

        print(f"order_p is {order_p}")
        print(f"order_q is {order_q}")

        if len(order_p) != len(order_q):
            return False

        for i in range(len(order_p)):
            if order_p[i] != order_q[i]:
                return False
        
        return True

        