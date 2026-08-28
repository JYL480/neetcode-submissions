# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
0. THis question pretty cool yah, this is a return and update question, because the 
- Diameter or the final answer can comme from where?
- The middle when visting other nodes. So this is pretty coool yah!!!
- Means waht???????
- This is a bot
- 
"""
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.ans = 0 

        def dfs( node):
            # Note that this is a bottom up approach which will require the use of DFS
            if not node:
                return 0

            # What are we doing, to fund teh max width is the max of left or right + 1 something liek this
            
            left = dfs(node.left)
            # The return value of the dfs is to return the height
            right = dfs(node.right)

            # No the width of the subtree is left + right hor!! This is tthe way right???? then 
            # WE are returning the maxx height

            self.ans = max(self.ans, left + right)

            return 1 + max(left, right)

        dfs(root)

        return self.ans



