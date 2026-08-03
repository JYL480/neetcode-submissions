"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
"""

0. for this we are using a hash map for deep copy yah!!!
- Where in each of the hassh map will be new Node() 
- Then you will just call
- If the .next = None, then we will use .get() yah as by default they will return NOne


"""


from collections import defaultdict
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        old_new = {None:None}

        curr = head
        
        while curr:
            # We will populate the new hs with the htingy
            
            old_new[curr] = Node(curr.val)
            curr = curr.next


        curr = head

        while curr:
            old_new[curr].next = old_new.get(curr.next)
            old_new[curr].random = old_new.get(curr.random)
            curr = curr.next


        return old_new[head]
    # Return the pointer ot the head











