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

        while list1 and list2: # Either both or none
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next

            elif list1.val >list2.val:

                curr.next = list2
                list2 = list2.next

            # You have to move up your curr 
            curr = curr.next


        curr.next = list1 if list1 else list2

        return dummy.next
      


                