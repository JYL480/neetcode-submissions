# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
1. To do detect if there is a cuyce


4. 2 ways to do this , 
We can either use hash set, to those that we have seen, but this would be O(n) for both
or fast and slow pointer which is O(1) for space

"""

# Oh store the haed itself, then you would know it unique or not LOL
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False




