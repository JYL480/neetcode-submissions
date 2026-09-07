# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


"""
0. lets redo this stupid question yah
- What do they wan ?
- They want to keep revesering every kth group and join back
- Fkin stupid
- Well the intuition is that we hav the??? the wafd?
- We can use the reveser node thingy
- And the get_kth function that reduces the value of k iteratively
- Also note that we need to use some ummy node for this yah
- where I will sever getkth revese and reattach and move up somehting liek that 



"""

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Because the OG head changes, wso we will have to create a dummy node for this yh 
        dummy = ListNode(0, head)
        # Note how this pointns yah it is a new node right before
        prev_grp = dummy # So in thee code later you will have to be prev_grp.next something liek that

        while True: # Yah from what I rmb it is while true with a break yah inside, break when there is very liittle number of nodes left to reveser
            
            kth = self.get_kth(prev_grp.next, k)

            if kth == None:
                break # Meaning we dont have enough nodes left

            # So now we have kth and prev_grp yah 

            # WE would sever first then do a reverse yah 
            next_grp = kth.next
            kth.next = None

            # Then we will reveser the prev gropu yah 


            old_head = prev_grp.next
            
            new_head_reversed = self.reverse(old_head) # So now old head will be the tail, we will keep prevgrp stricyly as prev grp
            
            prev_grp.next = new_head_reversed # we want to move up the as this becomes the new head
            old_head.next = next_grp

            prev_grp = old_head

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
        # How do this shit, we get kth?? IDK 
        # URMMMMM what do we do?
        curr = head
        # This question want use to keep movingtand ffind the pointer at which we are at the correct node??

        while curr and k>1:
            curr = curr.next
            k -= 1
        
        return curr





