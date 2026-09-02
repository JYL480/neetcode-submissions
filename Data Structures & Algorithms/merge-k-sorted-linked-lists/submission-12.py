# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
- Lemme do this for fun yab
"""


class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        res = []
        if len(lists) == 0 :
            return None

        while len(lists) > 1: # Becos we keep halfing this shhit until it becomes 1 
            res = []
            for i in range(0, len(lists), 2): # WE will jump in pairs yah
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None

                res.append(self.merge(l1, l2))
            
            lists = res

        return lists[0]

        
    def merge(self, l1, l2):
        # I pretty sure we can do this question with a heapq but this is okay yah 
        dummy = ListNode()
        curr = dummy


        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                # Move up the l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next

            # Ii have to move up the curr
            curr = curr.next


        # Have to merge if unqueal length yah 
        curr.next = l1 if l1 else l2

        return dummy.next





