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

from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        q = deque([root])
        
        level_size = len(q)
        # Invaraicen is that at the at the start of each for loop, it will contain all the node in that level
        while q:
            for _ in range(len(q)):
                node = q.popleft() # This will be make it O(1) yah with deque
                node.left, node.right = node.right, node.left
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return root

            

