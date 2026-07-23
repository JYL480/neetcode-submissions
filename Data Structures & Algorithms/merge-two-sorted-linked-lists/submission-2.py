# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""

0. Man this is so fckin complicated bruh

- anywasy, merge to into a new linked list
- We have to create a new dummy and tail listNode

- How would we solve this?

4. pattern?
- if its the same then 
- Note that we have to exahust both list. the list may not be the same length yah

"""


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        tail = dummy 

        while list1 and list2: # So eeither one is empty then break or both....
            
            if list1.val <= list2.val: # Here we want list1 val to be less than list2 
                tail.next = list1
                list1 = list1.next
            
            elif list2.val < list1.val:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next 









                