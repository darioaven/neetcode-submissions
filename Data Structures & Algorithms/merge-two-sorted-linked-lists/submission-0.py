# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        curr, head = None, None
        
        cnt = 0
        while list1 != None or list2 != None:
            if list1 == None:
                node = list2
                list2 = list2.next

                
            elif list2 == None:
                node = list1        
                list1 = list1.next

            else:
                if list1.val < list2.val:
                    node = list1
                    list1 = list1.next
                else:
                    node = list2
                    list2 = list2.next

            
            if cnt == 0:
                head = node
                curr = node
            else:
                curr.next = node
                curr = node
            cnt += 1
        return head