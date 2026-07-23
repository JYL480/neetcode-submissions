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

4. What to do ?


"""


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        curr = head
        seen = {}
        while curr:


            seen[curr.val] = 1 + seen.get(curr.val, 0) 
            
            if seen and seen[curr.val] > 1 and curr.next != None:
                return True


            curr = curr.next
            print(seen)

        return False




