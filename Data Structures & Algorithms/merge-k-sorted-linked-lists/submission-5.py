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
        
        # okay so this is a new thingy questio
        # Wopullld just merget the merge thingy, so it slike a divide and conquer ts

        # We look at n withlogN merging for this?yeah ii gu for while N, until somethhing becomes the e nd loh so it will be that righ 
        # How many time can we reduce k by 2, then you will have a binray tree whiich is logk


        # Edege case uh

        if lists == None or len(lists) == 0:
            return None

        # We want to see how many times I can divide the thing by, for binary search its logn whle 
        while len(lists) > 1: 
            res = []
            for i in range(0,len(lists), 2): # we will be working in paris
                l1 = lists[i]
                l2 = lists[i+1] if (i + 1) <len(lists) else None
                res.append(self.mergeList(l1, l2))
            
            lists = res # oh this is for the while loop to check. Then get the first element as this will be start of the pointer
        return lists[0]

    def mergeList(self, list1, list2):
        

        dummy = ListNode()
        curr = dummy
        
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next= list2
                list2 = list2.next
            
            curr = curr.next

        if list1 == None:
            curr.next = list2
        elif list2 == None:
            curr.next = list1
        return dummy.next
            





        