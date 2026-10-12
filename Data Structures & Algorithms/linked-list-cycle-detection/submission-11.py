# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
0.  For this what i know immediatley that we ahve to use the fast and slow pointer. 
- Bceuase eventual;y fast will lap 1 round and catch up to the slow. 
- Thne it will be a cycle. 
- Take note yah

"""

# Oh store the haed itself, then you would know it unique or not LOL
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head
        if not head:
            return False

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

            if fast.val == slow.val:
                return True

        return False


