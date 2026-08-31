# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



"""
0. YOu must know where your dummy node is pointing towards yah, this is very important!!!
- You need to when you are curr = dummy, curr is pointing the listNode(o, head) yah 


- So this question requires you the get the kth node and do a reversal 
- Then you need to have to spllit 
- Which requires 4 thing 
- kth - sever, reverse, attach back, move the pointer up

- SOmething oike that


"""

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    
        # for heere we need to creatae a new dummy node if im not wtong

        dummy = ListNode(0, head) # So dummy is new node with value 0 
        prev_grp = dummy


        # WE have to pass in curr.next yah
        kth = self.get_kth(prev_grp, k)

        while True:

            kth = self.get_kth(prev_grp, k)
            if not kth: 
                break
            next_grp = kth.next
            kth.next = None
            # Then you will sever, rev, attach and move up pointer
            
            reverse_head = prev_grp.next # THis will be new tail
            new_head = self.reverse(reverse_head) # This prev head will become the tail
            
            # now you got attach back 

            reverse_head.next = next_grp
            prev_grp.next = new_head


            prev_grp = reverse_head # Move the prev_grp to revers_head, we want the thing beore?

        return dummy.next

            


            

    def reverse(self, head):
        prev, curr = None, head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        return prev


    def get_kth(self, head, k):
        # How do do this
        
        curr = head
        while curr and k>0:
            curr = curr.next
            k -=1
        return curr
    
    
    
    
    
    
    