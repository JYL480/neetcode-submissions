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
        # If we are doing the recusrive one than it will be DFS recusrive yah 
        # Then we will be changing the swapping the node here where you would do the inplace thingy i think....

        # You must have an ending condition yah 
        # you must have you wiill be doing in pre and post order yah 
        # You must have root.left first then right yah. Something like that!!

        # Next will be doing DFS - iterative and BFS - iterative 
        # Pre and post order for DFS iterative is very similar to BFS deque yah, it is alsmot the same, but we are doinf DFS LIFO yah, something liekt ath hor 
        
        if not root:
            return None
        stack = [root]

        while stack:
            node = stack.pop()

            # We will do right first then left yah, so that left can be on top as we are doing LIFO 
            node.left, node.right = node.right, node.left
            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)

        return root