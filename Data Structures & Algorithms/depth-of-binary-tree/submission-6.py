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

        stack = [(root, 1)] # I would assume we are using not inorder, deoes not really maater pre order also can # it has to start with depth 1 yah, because, this is starting from there mah
        max_depth = 0
        # Note that last value is the higest valuel??
        while stack:
            node, depth = stack.pop()
            max_depth = max(depth, max_depth)


            if node.right: # Because we are just maxing does not really matter
                stack.append((node.right, depth + 1))

            
            if node.left:
                stack.append((node.left, depth + 1))


            

        return max_depth





