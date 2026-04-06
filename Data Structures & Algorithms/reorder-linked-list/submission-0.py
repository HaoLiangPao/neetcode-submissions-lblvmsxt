# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. Split the list into two parts (forward order) and (backward order, needs revers operation)
        slow, fast, count = head, head, 0
        while fast:
            count += 1
            fast = fast.next
            # print(f"fast is {fast.val if fast else 'None'}")
            if count > 0 and count % 2 == 0:
                slow = slow.next # Slow shall indicate the end of the forward order list
                # print(f"slow is {slow.val if slow else 'None'}")
        
        node = slow.next
        slow.next = None # This will be the None for the final linked list

        # 2. Reverse the backward order list
        prev = None
        while node:
            tmp = node.next
            node.next = prev
            prev = node
            node = tmp
        
        # 3. Merge the two lists
        dummy = ListNode(0)
        pointer = dummy

        left, right = head, prev
        while right:
            # First append forward order
            tmp1 = left.next
            pointer.next = left
            pointer = pointer.next

            # Next append backward order
            tmp2 = right.next
            pointer.next = right
            pointer = pointer.next

            # Update both lists
            left = tmp1
            right = tmp2
            
            # print(f"left is {left.val if left else 'None'}")
            # print(f"right is {right.val if right else 'None'}")

            # print(f"pointer is {pointer.val if pointer else 'None'}")

        
        # When odd #nodes, forward will have 1 more element
        if left:
            pointer.next = left






