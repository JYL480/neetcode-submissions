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

            # Urmm we just need to sever revesrse and reattach and move up 4 things 

            next_grp = kth.next
            kth.next = None

            reverse_head = prev_grp.next # Tail
            new_reverse_head = self.reverse(reverse_head) # beacome head

            # reattach now?/
            prev_grp.next = new_reverse_head
            reverse_head.next = next_grp

            # Move up?
            prev_grp = reverse_head


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







