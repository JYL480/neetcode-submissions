# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
0. Now wtf is this!!
- This iimmdialteay when we loo at the riht side, we can think of this a the last item in iterative BFS 

1. What do they want?
- Is to find the right 
- Somehting like that yah 
- Which should be easy to do!

2. edgcase


4. Should be quite simple for this yah


"""

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        q = deque([root])

        while q:
            lvl_size = len(q)
            for _ in range(lvl_size):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            res.append(node.val)

        return res


