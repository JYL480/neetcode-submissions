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
        dummy = ListNode()
        curr = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1= list1.next
            else:
                curr.next = list2
                list2 = list2.next

            curr = curr.next # To move up the curr pointer yah 

        # Themm you havee the remainding thingy

        curr.next = list1 if list1 else list2

        return dummy.next
 



                