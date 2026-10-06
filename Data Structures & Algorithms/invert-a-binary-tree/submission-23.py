# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
- Okay now lets try all three methiids righ !! Thts cool i think!

DFS - Iterative
DFS - Recursive
BFS - Iterative
"""

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return None
        stack = [root]

        results = []

        while stack:
            node = stack.pop()
            
            node.left, node.right = node.right, node.left

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)


        return root