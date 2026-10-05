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
        # Then we area doign in order here, somehting special 
        # Which will be what, special, rmb you go all the way then or someht hg

        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            # We are at the veyr bottom liao 
            curr = stack.pop()

            curr.left, curr.right= curr.right, curr.left
            
            curr = curr.left

        return root