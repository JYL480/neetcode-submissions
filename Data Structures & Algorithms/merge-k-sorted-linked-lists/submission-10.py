"""
0. Lets do this again. 
- Okay this would require mergeing of sorted linkedd list multiple times
- So we would have to create the algo for this and yeah like that lohhh


4. So what now?
- Okay we will do something about it yah 
- create a functiotn for the merging hopefully you will rmb
- Lets go through the cheatsheet once more okkay!


5. The merging of 2 sorted LL is O(N + M ) or just O(N)
- We are working in a binary tree, so this will be NlogK, where k is the number of arras inside yah!!!!




"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# I think will merge k maybe have to use deque or heap for this? If its top k, 
# Prob will need some dummies for thi syah

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Okay now that you have these 2, then you need to merget btrween them 

        # Right this is binary thingy yah, you walpwakys trying to divide this sht by 2 iver cane over gaini
        # need to some edge cases here?

        if len(lists) == 0: 
            return None

        while len(lists) >1: # To allow for continuous division hor 
            res = []
            for i in range(0, len(lists), 2): # This will do in pair yah 
                l1 = lists[i]
                l2 = lists[i + 1] if len(lists) > (i + 1) else None
                res.append(self.mergeL(l1, l2))
            lists = res
        
        return lists[0]


    def mergeL(self, l1, l2):
        dummy = ListNode()
        curr = dummy 

        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next

            curr = curr.next

        curr.next = l1 if l1 else l2

        return dummy.next












     