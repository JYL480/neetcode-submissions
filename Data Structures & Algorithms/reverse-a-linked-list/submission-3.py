# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""

0. Okay i need to finish this shit bruh , so annoying..

1. What do they want?
- They want to reveser the linked list


skip

4. Pattern?
- Okay we need to havae  a prev and a curr pointer yah to reverse everyshit..

"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr: # I will be moving curr up yah 
            temp = curr.next
            curr.next = prev # THis is the one swapping the arrow
            # Need to deal with both the 2 pointers, becuase we swap, we need to swap both sides hor
            prev = curr
            curr = temp

        return prev

  
        


        
