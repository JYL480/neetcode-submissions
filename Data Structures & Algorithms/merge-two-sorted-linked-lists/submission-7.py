# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
0. Should be easy fopr you uh!!!
- Do this with your eyes closed!

"""


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # I think i sort of rmb, we want to return a merge linked list yah 
        # we have to createa  dummy note for the start yah 
        dummy = ListNode()
        curr = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                # We are plaing the node to the new thing
                curr.next = list1
                list1 = list1.next

            else:
                curr.next = list2
                # Then we will move up the indiv list
                list2 = list2.next

        #whne we have uneven length of the list right then we will do this
            # We have to move up the dummy as weill yah 
            curr = curr.next

        if list1:
            curr.next = list1 
        else: 
            curr.next =  list2

        return dummy.next


                