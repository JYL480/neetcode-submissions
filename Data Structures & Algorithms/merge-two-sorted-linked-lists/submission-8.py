# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
0. Should be easy fopr you uh!!!
- Do this with your eyes closed!
- this equeisotn wants me to merget the list into 2 and it should be sorted yah 

4. we have to create some dummy node for this as the head, 
- We hav to move the curr iindiiducal list pointer updarwawds yah 
- And so on....

"""


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy 

        while list1 and list2:
            # Then we will create the new LL based n the the val 
            if list1.val<= list2.val: # list1 vall wil lbe better loh

                curr.next = list1
                list1 = list1.next
            
            elif list2.val < list1.val:
                curr.next = list2
                list2 = list2.next

            # We have to move this curr up yah 

            curr = curr.next 

        # if we have uneven length of the thingy

        if list1:
            curr.next = list1
        else:
            curr.next = list2

        return dummy.next



        