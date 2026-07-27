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


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hash_set = set()

        while head:
            if head not in hash_set:
                hash_set.add(head)
                print(hash_set)
            else:
                return True
            head = head.next
            

        return False
   