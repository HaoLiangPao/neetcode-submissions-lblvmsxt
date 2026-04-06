# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getLinkedListLength(self, head: Optional[ListNode]) -> int:
        # Iterate through the linked list
        node = head
        counter = 0

        while node:
            node = node.next
            counter += 1
        
        # counter shall equal to the total length of the list
        return counter

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Edge Case
        if head.next is None:
            return None

        length = self.getLinkedListLength(head)
        
        node = head
        counter = 0
        target = length - n

        # Removing the head node
        if target == counter:
            return head.next

        # Otherwise
        while counter < target:
            pre = node
            node = node.next
            counter += 1
        
        pre.next = node.next if node else None

        return head
        
