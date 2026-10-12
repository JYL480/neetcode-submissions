# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
0.
- Lemme do this for fun yab
- How the fk do we do this shit yah
- Merge K sorted linked list, 
- What we will be doing is divide and conquer this shit, which is good yah 
- What is divide and conquer this shit?
- But we have theh merge sorted list and
and thendicide conquer


5. COmplexity 
Time((M + N)log (len(list)))
space: O()


"""


class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists:
            return None

        dummy = ListNode()
        curr = dummy
        res = []

        # Righ we ahve to keep doignthis for a while yah 
        while len(lists) >1:
            res = []
            for i in range(0,len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i + 1) < len(lists) else None
                res.append(self.merge(l1, l2))

            lists = res

        return lists[0]

    def merge(self, l1, l2):
        dummy = ListNode()
        curr = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next

            elif l1.val > l2.val:
                curr.next = l2
                l2 = l2.next

            curr = curr.next

        curr.next = l1 if l1 else l2

        return dummy.next


