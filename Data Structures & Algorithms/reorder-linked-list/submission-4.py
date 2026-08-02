# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""

0. This would have to use the fast and slow pointner 
- Plus reversal of linked list
- Plus clean cut of the Linked List 
- And the combine them into a single list

"""

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # This will be the fast and alsow pointer to find where is the mid point
        # WE will use head.next first as the fast, as we wand the sevond half i
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        
        second = slow.next
        slow.next = None

        # Here will be the rerversal 
        
        prev, curr = None, second

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        
        # Now we will combine
        second = prev
        print(head.val)


        while second: # it will be while second, because the second half is much shorter!!! if its 
            tmp1, tmp2 = head.next, second.next

            head.next = second
            second.next = tmp1

            head = tmp1
            second = tmp2
            




