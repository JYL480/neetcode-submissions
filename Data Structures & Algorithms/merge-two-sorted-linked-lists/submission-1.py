# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""

0. Likely we have to create a new lists node for this yah


4. Know when to add which value of the list nnode
- Move the tail 
- And how to deal when 1 o the node is alreadyexahsted...


"""


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
            
        return dummy.next









                