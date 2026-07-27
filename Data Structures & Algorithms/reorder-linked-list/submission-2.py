# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
0. This one utilises a lot of techniques tgt. 
- Reversee the ll
- the sow and fast pointer thingy yah
"""

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow = head
        fast = head.next # The fast pointer will be one step head, so that we can can a the lower halfif we have even

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow # This will be the mid point 
         # THen we will reverse

        # We need to sever ths second half list?

        second = slow.next
        slow.next = None # So the first half points to None at the en

        prev = None
        curr = second

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # Then I will split them in half yah
        first = head
        sec = prev

        while sec:
            temp1, temp2 = first.next, sec.next
            first.next = sec
            sec.next = temp1

            first = temp1 
            sec = temp2






        