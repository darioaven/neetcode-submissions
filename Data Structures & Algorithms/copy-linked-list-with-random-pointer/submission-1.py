"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return None
        curr = head
        new_dict = dict()
        random_dict = dict()
        while curr:
            new_dict[curr] = Node(x=curr.val)
            curr = curr.next

        curr = head
        head_c = new_dict[curr]
        prev = None
        while curr:
            node = new_dict[curr]
            
            if curr.random:
                node.random = new_dict[curr.random]
            
            if prev:
                prev.next = node
            curr = curr.next
            prev = node
        return head_c 