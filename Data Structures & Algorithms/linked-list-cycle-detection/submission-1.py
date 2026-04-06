# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Save all the nodes that have been accessed
        record = set()
        index = 0

        while head:

            if head not in record:
                record.add(head)
            else:
                return True
            
            # print(f"head's value is {head.val}")
            # print(record[head.val])
            
            index += 1
            head = head.next

        return False