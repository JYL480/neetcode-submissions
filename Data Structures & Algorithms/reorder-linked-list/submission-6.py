# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""

0. Lets do this again for fun yah
- THis one is important to note that we can decide if we wat to choose the top half or the bottom half the shit 


4. What does it want?
- This one is teh slow and fast pointner
- And reversal of this shit
- And the combine them tgt yah 
- You mught to have a have to sever them poroperly as well yah 


"""

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # We want the bottom half of this shit
        slow, fast = head, head.next

        # fast will be one ahead first because we want to the bottom half yah 
        # So the1 the 1st half and 2nd half will either be same length or the 1st will be smaller!

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        
        # Now I want to sever them propelry yah 
        second = slow.next
        slow.next = None

        # Now I want  to reverse the second half

        prev, curr = None, second

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        
        second = prev
        first = head

        while second:
            tmp1, tmp2 = first.next, second.next

            first.next = second
            second.next = tmp1

            # Move them up
            first = tmp1
            second = tmp2
        
        

        






