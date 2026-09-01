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

        if not root:

            return  None
        q = deque([root])
        
        while q:
            for _ in range(len(q)): # So we will go through all this level yah
                node = q.popleft()
                node.left, node.right = node.right, node.left
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return root



        