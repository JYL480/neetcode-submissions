# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
0. First instinct this is a top down approach, where you have to pass down the counter and smallest value?
- So it will be top down DFS yah\


4. Pattern
- This should be okay rihgt,
- we are going to go through the node in order for this!!
- What do you mean in order?
- THen we just do the simple indexing
- so this is inorder DFS!!! 

5. complexity,
time: hiehght of the tree O(h) either logn or n 
space: o(n)
"""



class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        res = []

        def dfs(node):
            if not node:
                return 
            
            
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)

        dfs(root)
        return res[k-1]