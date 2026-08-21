# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
0. WHat is this question
- then wanty you to merget to sroted linked list
- return a single linked list yah
- So what now?
- It will be without this or that
- The length might be diff

4. SHould be quuite easy, you defineyneed to create a new dummy node to poinnt to the new thingy
- And then if it left ovetr, then you just on loh


"""


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()

        curr = dummy

        while list1 and list2:
            if list1.val <= list2.val: # Meaing , then if less than or same i will put 1 first
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next

            curr = curr.next

        # Then the remmainng shiit loh
        if list1 == None:
            curr.next = list2
        elif list2 == None:
            curr.next = list1

        return dummy.next







                