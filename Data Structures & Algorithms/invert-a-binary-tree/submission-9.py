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

        if not root:
            return None
        stack = []

        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()

            curr.left, curr.right = curr.right, curr.left


            curr = curr.left

        return root


        