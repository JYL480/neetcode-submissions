# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
Another warm up question yah 

- We want to change the arrows and them move up the pointer of prev and curr to the next
- How  to reverse, we are changing the directyion of the arrow, while moving the prev up


- Shuld be quite simple yah, Havent doen this in a while yah


"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, prev = head, None

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        return prev
        