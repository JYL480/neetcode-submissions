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
        curr = root
        stack = []
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left


            curr = stack.pop()

            curr.left, curr.right = curr.right, curr.left

            curr = curr.left


        return root