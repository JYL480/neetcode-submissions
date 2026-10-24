# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
- I think i cam do this one yah
- We are just doing a BFS deque traversal yah which is okay
with a first in first ou tyah thus we will use a dque 

"""

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([root])

        res = []

        if not root:
            return []

        while q:
            lvl_size = len(q)
            current_level = []

            for _ in range(lvl_size):
                node = q.popleft()
                current_level.append(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)


            res.append(current_level)

        return res