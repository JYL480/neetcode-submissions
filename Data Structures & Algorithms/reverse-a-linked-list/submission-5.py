# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
0. This has to be 

"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
     

        # Okay im reversing the arrows, so that I can move up oso!!!!
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
        
