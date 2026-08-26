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

"""

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [[root,1]]
        longest = 0


        while stack:
            node, depth = stack.pop()

            
            longest = max(longest, depth)
            print(longest)
            
            if node.right:
                stack.append([node.right, depth + 1])
                
            if node.left:
                stack.append([node.left, depth + 1])
        
        return longest


        
