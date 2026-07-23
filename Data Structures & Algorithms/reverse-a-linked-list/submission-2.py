# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
0. First off when you are doing a linked list question, when you craete a new linked list

- We will usualyy have a dummy and a tail node, Note that the initilalisation of these pointers are pointer to 0 
- Which is not what we want. 
- So when you return, you lklely have to retrurn the dummy.nexxt yah 

- Anyways this should be siple
- with this we are using a prev and curr, 
we will return the prev, annd the curr will keep moving

- I want to turn the arrow the opposite direction!!!
- Prev will evneatully reacch the end or become the new head hence making it to a diff thing


"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
     
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr # I will move prev up
            curr = temp # Then we will deal with the next node 
        return prev
        


        
