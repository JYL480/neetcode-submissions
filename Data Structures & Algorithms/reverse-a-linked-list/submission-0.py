# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
1. They want to return the pointer to the list, most of the time, you will return the pointer
- Which now points to the new head. And sincec we erevese this shit, then its
- So this is the main pointn you need to note when dealing with pointerss


4. How? We need something to move on, and next to point to the previous one

"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        # Note that the pointer direclty deals witht head, so if you change the pointer,you 

        while curr:
            nxt = curr.next

            curr.next = prev
            prev = curr
            curr = nxt
        return prev



        
