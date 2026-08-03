# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""

0. TLets do this again hor
- it good to practive the different techniques yah
- which are the fast and slow pointners
- reversal of linked lislt 

"""

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Note that with the fast and slow pointer, you will be using the fast.nenxt, such that slow will end earleier, you will either return the first half end pointer of the 2nd half start poinnter
        slow = head
        fast = head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        sec = slow.next
        slow.next = None

        prev, curr = None, sec

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        # Combine them tgt

        sec = prev
        first = head

        while sec: # We will do the sec becuase sec will be shorted yah 
            tmp1, tmp2 = first.next, sec.next

            first.next = sec
            sec.next = tmp1

            # WE need tp ov,e up the pointers
            sec = tmp2
            first = tmp1
        
        






