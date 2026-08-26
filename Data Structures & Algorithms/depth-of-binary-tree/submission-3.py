# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
0. WHat is tthis a binary tree to get the longest path
- Prob have to do a DFS iterative and recusrion bah 
- Then you willl have longest thingy?? IDK

4. DFS

5. Complexity 
- O(N), as you viisted all the nodes once
- O(N) N will be worst case or LogN for balanced


- Your stack and be [placed with a tuple or add some shit inside which acn help with the counting of the depth yah!!!
- This is super cool!!!

- LEts try with what BFS ieterative 


"""



from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque([(root, 1)]) # Like this?

        longest = 0 
        while q:
            for _ in range(len(q)):
                node, depth = q.popleft()
                if node:

                    longest = max(longest, depth)
                    q.append((node.left, depth + 1))
                    q.append((node.right, depth + 1))
        return longest