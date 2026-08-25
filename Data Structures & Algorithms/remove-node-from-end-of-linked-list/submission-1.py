# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        cnt = 0
        curr = head
        while curr:
            curr = curr.next
            cnt += 1
        
        node = head
        prev = None
        for i in range(cnt - n):
            prev = node
            node = node.next
        
        if not prev:
            return head.next

        if node:
            prev.next = node.next
        
        return head
        