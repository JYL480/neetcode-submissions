# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""

1. We can just get a pointer to directly to that node, so thats cool. HOHO 
- So that can be an option for us 9nin the futrue to the store the nodes in the list!

"""

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        left = dummy
        right = head

        for _ in range(n):
            right = right.next

        # Now its like a slow and fast pointer

        while right:
            right = right.next
            left = left.next
        
        left.next = left.next.next

        return dummy.next
