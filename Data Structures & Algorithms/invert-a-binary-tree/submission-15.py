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

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # If we are doing the recusrive one than it will be DFS recusrive yah 
        # Then we will be changing the swapping the node here where you would do the inplace thingy i think....


        # Ending conditoin 
        if not root:
            return None

        # We will swap tht ehtingy?
        root.left, root.right = root.right, root.left

        self.invertTree(root.left)

        self.invertTree(root.right)


        return root



        