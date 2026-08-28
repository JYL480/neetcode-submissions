# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
0. What can you d0?
- This question assk you do find the depth of tree which s just a return only type question
- The asnwer

- I will recap on this yah
- Using the 3 different thingy?
- 3 differnt algo i know of '
0 which sill be DFS iterative and recursive
and BFS



"""

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        