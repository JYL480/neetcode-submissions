"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
"""
0. Hmm what do they wanat?


1. They want you to copy the linked list!! HMM about what?
- return a pointer to a linked list, each of the new pointer will be have the neaxt and val and random?



"""


from collections import defaultdict
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur = head
        newtoold = {None:None}
        print(newtoold)

        while cur:
            newtoold[cur] = Node(cur.val)
            cur = cur.next

        # print(newtoold) # inside will have the new node
        start = head
        while start:
            newtoold[start].next = newtoold[start.next]
            newtoold[start].random = newtoold.get(start.random)
            start = start.next

        return newtoold[head]
    
        



