class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None
        
        # Mapping: Old Node -> New Node
        mapping = {None: None} 
        
        # 1st pass: Just create the nodes
        curr = head
        while curr:
            mapping[curr] = Node(curr.val)
            curr = curr.next
            
        # 2nd pass: Wire 'next' and 'random' using the map
        curr = head
        while curr:
            mapping[curr].next = mapping[curr.next]
            mapping[curr].random = mapping[curr.random]
            curr = curr.next
            
        return mapping[head]