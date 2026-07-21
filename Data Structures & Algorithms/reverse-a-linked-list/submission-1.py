# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
1. THis hsould be quite simple,
Rmb that when we are workgin with linked list, we are most of the time wokring with pointers

4. For this because we are reversing, likely we need a prev pointer and soemething else
previous and curr, for us to swap 
- Only when we prev, cur pointer then we can do something about it



"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev

        
