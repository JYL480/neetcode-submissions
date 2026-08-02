# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
Another warm up question yah 

- We want to change the arrows and them move up the pointer of prev and curr to the next

"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
     
        prev, curr = None, head

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        return prev
