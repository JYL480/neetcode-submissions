"""
0. This one is using multiple differnent techs yah
- There is like a pattern liekreversiang  and they keep getting that node ig




4. Create 2 functions
- reverse
- getkth
- And yeah thats about it loh

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # yeah thats about it i think 

        dummy = ListNode(0, head)
        prev_grp = dummy # So this will be prev, the on that will be reversseed

        while True:
            kth = self.get_kth(prev_grp, k)

            if not kth:
                break


            # Need to sever first to reverse4
            next_grp = kth.next # as a tmp to store 
            kth.next = None # Sever

            prev_head = prev_grp.next # This will be point to the head
            reversed_new_head = self.reverse(prev_head)

            # Now prev_head will be the tail, new head will be head

            prev_head.next = next_grp # connect them tgt 
            prev_grp.next = reversed_new_head # The prev_grp pointer point to here
            
            # I will move up after reversing, which is to move up the the new head that wants to be reversed?
            prev_grp = prev_head


        return dummy.next


            




    def reverse(self, head):
        prev, curr = None, head

        # Note that in the main code you will automatically shifr th head to tail
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        return prev
        

    def get_kth(self, head, k):
        curr = head
        while curr and k>0:
            curr = curr.next
            k-=1
        return curr







