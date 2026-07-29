# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
0. this one is terrible uestion 
1. You have to use the fast and slow pointer
2. cut off properly and then reverse the pointers method
"""

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow = head
        fast = head.next # We do this, ecayse we want the when even numbers, the pooniter will belong to the 1st half 

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None # Now i serverd in properly


        
        prev = None
        curr = second

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        first = head
        second = prev

        # Now i join them tgt
        

        while second:
            tmp1, tmp2 = first.next, second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2
            






        