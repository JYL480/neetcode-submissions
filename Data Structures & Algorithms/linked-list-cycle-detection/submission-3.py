# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
1. What does the question want?
- Return a boool

- Check whether there is cycle in LL
- when ll.next = index-th node if its -1 then it will be pointing to a null
- if it >= 0 then it will be good?
- IDK

2. 

4. New algo unlock yay. This will be for the tortoise and rabbit algo. 
Where you will have a slow and fast pointer
- Because if there is pointer slow and fast, evntually both will catch to each other. 
- Bbecuase it will be the disnat cebetween them or the ma lenght of the ll which is n 
O(N) and no O(1) for space complexity yay whcih is much b etter

"""


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
       
        slow, fast = head, head

        while fast and fast.next: #why need 2 because you are dealing with this current and the next one need to check if you are ahead or not whether it null or not

            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True
        return False