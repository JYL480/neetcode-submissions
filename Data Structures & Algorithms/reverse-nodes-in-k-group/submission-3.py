"""
0. Intuition?
- Hvae to use the N gap to get to the middle but first You have to check LOH
- Then you have to use the reversal of LL
- You also have to sever it properly then combine them tgt? IDK ,okay you can jsut to do a for loop loh

1. I completely did not understand what does the question want brother!!!
- What isit?
- Urmm, you are moving, If its damn long, you will get the k 
revers and keep merging the kk number of nodes, I guess we have ther reversr function and get the k node

2. edge cases?

3. Naive? urmm i hhinestlu i dont a naive loh


4. What is the pattern?
- you can just do the above i think


5. Complexity?
- Urmm wiill be what IDK 
O(N) for spliting + O(K)  for the moving thats about it?
O(1) for space?

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
       
        # Okay I will have while loop for this hsit yah

        dummy = ListNode(0,head)
        grp_prev = dummy

        while True:
            kth = self.get_kth(grp_prev,k)
            if not kth:
                break
            
            next_grp = kth.next
            # Sever prop
            kth.next = None

            grp_head = grp_prev.next

            # Then you will reverse?
            new_head = self.reverse(grp_prev)

            grp_prev.next = new_head
            grp_head.next = next_grp

            grp_prev = grp_head

            # Then I will add them tgt?
        return dummy.next
            
    

    def reverse(self, head):
        prev, curr = None, head

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp 
        
        return prev

    def get_kth(self, curr, k):

        while curr and k>0:
            curr = curr.next
            k -=1
        return curr









