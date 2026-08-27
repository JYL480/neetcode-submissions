# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
-This should be an easy question yah, should be okay for you do do. 
- We are basically doing the merge in for sroted list. 
- logN x (M+ N) Omsehitng liekfor the time comexoty




"""

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Now we got do the binary mergeing thingy yah
        # Whihc is how, do we need create new hinary yah 
        dummy = ListNode()
        curr = dummy

        if len(lists) == 0 :
            return None


        while len(lists) > 1: # meaning we still ca merge tgt 
            res = []

            for i in range(0,len(lists),2): # Cause we are doing in pairs
                l1 = lists[i]
                l2 = lists[i+1] if (i + 1) < len(lists) else None

                res.append(self.merge(l1,l2))
            lists = res

        return lists[0]
            




    def merge(self, l1, l2):
        dummy = ListNode()
        curr = dummy

        while l1 and l2:
            if l1.val<= l2.val:
                curr.next = l1
                l1 = l1.next
                # So you will point curr to the next and move l1 p 

            else:
                curr.next = l2
                l2 = l2.next

        # To deal with uneven len 
            # I have to move the curr as well ya 
            curr = curr.next

        curr.next = l1 if l1 else l2

        return dummy.next



