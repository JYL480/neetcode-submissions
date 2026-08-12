# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
0. This is an easy qurestoin
- They want you to remove a certain node in the linked list 


1. Want you to return a linked list node with the node removed


3. Complexity 
- this will be the n gap slpw fast pointer type shit 
- while will be O(N)
O(1) spaec


4. Pattern?
- N gap 2 pointners

- You will have a for loop to move that pointer whihc is N gap away then you move allwy the way to the end

- Ohthis is important, if any thing witin
"""

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        

        # We have to create a dummy node when removing the nodes within the lLL

        dummy = ListNode(0, head)
        slow = fast = dummy

        
        for _ in range(n+ 1):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        print(slow.val)
        print("ASD")
        # Now that slow points to the thing we want to 1 before too thing we want to remove

        slow.next = slow.next.next

        return dummy.next










        