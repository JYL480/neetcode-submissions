# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
0. This needs to second nature bruh

To revrse this shit, you ahve to know about what isit like to reverse
- Menaing all the arrows are pointinng in the other direction!!

4. You would need a prev and curr to move yah


"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev # This to point back wrds
            prev = curr # This for the prev to become the next 
            curr = temp
        return  prev
  
        


        
