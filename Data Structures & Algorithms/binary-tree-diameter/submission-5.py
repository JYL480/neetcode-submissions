# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
- You have to add them tgt to get the returned value wdith tgt i guess. IDKk 
- We will see how this works
"""
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # We have a global vairable to update
        self.ans = 0 

        def dfs(node): # Always the bottom up we will need to find out the ending codniton yah 
            if not node:
                return 0 # Because we gonna + 1 later
            
            left = dfs(node.left)
            right = dfs(node.right)


            # We have to get the width in btwn, because the answer are from here yah 

            self.ans = max(self.ans, left + right)  # Each of the left + right will reutrn something yah 
            return 1 + max(left, right)

        dfs(root)

        return self.ans

            


