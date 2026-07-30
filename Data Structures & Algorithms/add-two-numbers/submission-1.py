# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        cur = res
        # Need to know how to carry over
        carry = 0

        while l1 or l2 or carry: # we do or because l1 and l2 can be of different length!!!
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0 

            val = v1 + v2 + carry # Intially at start will be 0 

            carry = val // 10 #Right can be more than 1 LOL
            val = val % 10 #First digit

            cur.next = ListNode(val)


            cur = cur.next
            if l1: 
                l1 = l1.next 
            if l2: 
                l2 = l2.next

        return res.next





  
