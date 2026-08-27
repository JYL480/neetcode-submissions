# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
0. What is inversiion
- You want to see the sub tree, go to all the nodes available then you will swap the child
- We can usse DFS for this? 
- We can use recursion yah

"""

from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Lets go thgrough so that you will rmb the algo yah
        # What this question want ?/
        # Lets try with dfs 2 and bfs 2 
        # Whay isit??? IDK I want to kmd fml!!!
        # Lets do BFS first with a dque yah 
        q = deque([root])
        # We are doing  bbased on what?

        if not  root:
            return None

        while q:
            results = []
            for _ in range(len(q)):
                node = q.popleft()
                # Then i swap here uh
                node.left, node.right = node.right, node.left

                # Add the thingy isnits left witll be first 
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return root



