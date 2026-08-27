# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
0. is the longest path or the most number of egdes?
- THis has to be done in pre oder right 
- If you in order?/
- left root then right

"""
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # The dfs will be return the hegith in the sub stree

        res = 0

        # This is done recursively, here we will return teh ehight sort of yah
        def dfs(curr): 
            if not curr:
                return 0
                
            left = dfs(curr.left)
            right = dfs(curr.right)
            
            nonlocal res 
            res = max(res, left + right) # This is the width? Of that sub streew which is will be the answer

            # But we are return the hegith of that subtree to be +1 to the parent 

         
            return max(left, right) + 1 # Plus willl be for the ehgiht 

        dfs(root)
        return res
    