# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(-101)
        pointer = head

        if not list1: return list2
        if not list2: return list1

        while list1 and list2:
            print(f"list1 value is {list1.val}, list2 value is {list2.val}")
            # Compare each node in list1 and list2, append them in increasing value order
            if list1.val <= list2.val:
                pointer.next = list1
                list1 = list1.next
            else:
                pointer.next = list2
                list2 = list2.next
            pointer = pointer.next
        
        if list1:
            pointer.next = list1
        elif list2:
            pointer.next = list2

        return head.next