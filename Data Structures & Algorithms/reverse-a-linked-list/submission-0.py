# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        newHead = None

        # print(f"Original head is {head.val}")

        while head:
            tmp = head
            head = head.next

            # Update new linked list
            tmp.next = newHead
            newHead = tmp

        return newHead