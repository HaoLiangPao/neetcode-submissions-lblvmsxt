# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0)
        node = result
        carry_over = False

        # Merge two digit
        while l1 and l2:
            local_sum = l1.val + l2.val
            
            # Carry over
            if carry_over:
                local_sum += 1
            
            cur_val = local_sum

            # Check if forming new carry over
            if local_sum >= 10:
                cur_val = local_sum - 10
                carry_over = True
            else:
                carry_over = False
            
            node.next = ListNode(cur_val)
            node = node.next
            l1 = l1.next
            l2 = l2.next
        
        # If l1 or l2 is shorter, keep whatever the left
        while l1:
            # First Check if carry over
            cur_val = 1 if carry_over else 0
            cur_val += l1.val
            if cur_val >= 10:
                cur_val -= 10
                carry_over = True
            else:
                carry_over = False
            node.next = ListNode(cur_val)
            node = node.next
            l1 = l1.next
        
        while l2:
            cur_val = 1 if carry_over else 0
            cur_val += l2.val
            if cur_val >= 10:
                cur_val -= 10
                carry_over = True
            else:
                carry_over = False
            node.next = ListNode(cur_val)
            node = node.next
            l2 = l2.next

        # Edge Case: two lists are at the same length but exist a carry_over
        if not l1 and not l2 and carry_over:
            node.next = ListNode(1)

        return result.next
