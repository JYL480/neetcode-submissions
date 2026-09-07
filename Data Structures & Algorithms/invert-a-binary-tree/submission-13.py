# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
0. Let me have all the thingy yah!!!
- Lets try all the algo we can work with hor!!!

- DFS iterative
- DFS Recrusive
- BFS iterative


- Now we will tyr DFS iterative yah which is what?
- We have 3 differet options yah !! Which is inorder, pre order and postorder
"""

from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # OKay now we have iterative DGFS as well, this is a FIFO
     
        # Lets not do inorder first, abiy cofusing yah
        # lets do thingy first wad?

        # What is next which will be inorder urmm, we will move down all the way to left first, then we append 
        # if root == None:
        #     return None

        stack = []
        curr = root
        while stack or curr:
            while curr:

                stack.append(curr)

                curr = curr.left


            curr = stack.pop()

            curr.left , curr.right = curr.right, curr.left
            curr = curr.left
        return root






        