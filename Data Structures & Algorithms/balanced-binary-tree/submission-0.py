# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
0. So this is a bottom up approach which returns + update global state of a bool yah 
- cos the answer can come from sub tree if I am not wrong yah
- So take note of this
- This will def be a reursive prob i think


4. Will be using  recusive prob
- Each root will return the diff between left and righ t
- If it is > 1 then update the bal flag?????
- Then return the max of the left or right Im wrong + 1 to add on to the next node in the height!!!
- HOHOHOHO

"""

import math

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.bal = True

        def dfs(node):
            if not node:
                return 0 


            # What is this bruh IDKKKKKK Kill me now!!
            left = dfs(node.left)
            right = dfs(node.right)

            if abs(left - right) > 1:
                self.bal = False

            return 1 + max(left, right)

        
    
        dfs(root)
        return self.bal










