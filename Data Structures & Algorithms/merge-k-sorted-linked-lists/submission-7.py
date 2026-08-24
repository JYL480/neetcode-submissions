"""
0. OKay we will try this question again yah
- Meaning that we will have this thingy?
- Wihch is like a binary loop thingy, we we keep combinign over and over again
- So you know the 

4.  You will create a separate function to merget the linked list tgt
- And then you will have the binray looop thingy for merging, which is while len(lists)>1:
somehting liekk this



5. You knnow the height of the binary tree, which is logn and when you merge will be O(N + M) O(M)
Mlogn this is the complexity 
- O(N) for the space bah, cause you would need to store some ht elinked list to count the len?

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

        # You have to handle some edege vases ig, if they are empty in the first place

        if len(lists) == 0 or lists == None: # Can lists == None?
            return None

        while len(lists) > 1:
            res = []
            for i in range(0,len(lists), 2): # You will do in  pairs, have a for loop for this
                list1 = lists[i]
                list2 = lists[i+1] if len(lists)> i + 1 else None

                res.append(self.mergeList(list1, list2))
            lists = res

        return lists[0]

    def mergeList(self, list1, list2):

        dummy = ListNode()
        curr = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next

            curr = curr.next

        curr.next = list1 if list1 else list2

        return dummy.next











     