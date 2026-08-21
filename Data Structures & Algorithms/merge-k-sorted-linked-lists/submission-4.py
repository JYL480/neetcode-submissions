"""
0. What do they want?
- They want you to return a linked list, prob a dummy.next for this 
- where you will return a sorted linked list from different linked list yah
- urmmmm yah 
- so have to use a dummy node for this?
- Urm; have to do it in n * k
- I saw a merge K sorted, maybe we can put in a min heap and then sort it out?
- IDK we will see, it isnt really like top K 


1. Have to return a linked list, in a sorted linked list
- sheet, this seems complicated????

2. edge?
- the head can be replaced, so best to have a .dummy.next node to deal with this?

3. naive
- if we dont care abouthtis, we can just ignore that and get a normal list, them connext them?

4. Pattern?
- n*k complexity uh??
- to heapify the list it will be a o(N) times yah
0. What this one 



"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# I think will merge k maybe have to use deque or heap for this? If its top k, 
# Prob will need some dummies for thi syah

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        ll = []

        for i in lists:
            while i: #ah, right we need to move the nodes loh
                ll.append(i.val)
                i = i.next
        ll = sorted(ll)

        # You would need to create a dummy node what, to be ablt ro return the hsit? no?
        dummy = ListNode()
        curr = dummy

        # Then you wil move with the curr
        for j in ll:
            curr.next = ListNode(j)
            # I need tomove up 
            curr = curr.next
        return dummy.next


        