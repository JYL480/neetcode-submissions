# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
0. Note that because sometime
- nnote that we can do this with the fast and slow concept, but such that the 2 pointers are nth position away from each other
- Note we shouldnt try to use the head to move but rather use the dummy node for thhis
- Why dummy node, note that we need to know the prev and not the current, because we need to link them up propelry

4. using a dummy node for thiis yah

"""

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode()
        dummy.next = head

        slow = dummy
        fast = dummy

        for _ in range(n):
            fast = fast.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next

        # Slow is that poistion we want to remove
        slow.next = slow.next.next

        return dummy.next