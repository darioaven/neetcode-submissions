# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        curr1, curr2 = l1, l2
        remainder = 0
        prev = None
        head = None
        while curr1 and curr2:
            val = curr1.val + curr2.val + remainder
            
            if val >= 10:
                remainder = 1
            else:
                remainder = 0

            val = val % 10
            curr1 = curr1.next
            curr2 = curr2.next
            node = ListNode(val)
            if prev:
                prev.next = node
                prev = node
            else:
                head = node
                prev = node

        curr = None
        if curr1:
            curr = curr1
        
        if curr2:
            curr = curr2
        
        while curr:
            val = curr.val + remainder
            
            if val >= 10:
                remainder = 1
            else:
                remainder = 0

            val = val % 10
            curr = curr.next
            node = ListNode(val)
            
            prev.next = node
            prev = node
            
        if remainder > 0:
            prev.next = ListNode(1)

        return head
        