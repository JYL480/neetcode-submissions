# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
0. It is has to be some form of botto up, 
- I need to know the left and right, before i return a valid thigny
- Bottom up dfs will be post order. Left, right thne middle

1. What do thtey want ?
- They wnat to check whether the tree si a valid BST
- So th eledt has to be less and the right has to be more!!!
Becos the relationshop is going down, so 
- The left and right down there has to be in teh same rs overall?
AS long you are in the right subtree, you will always be bigger likewise as long you are in the left subtree
- YOu will alwys be smaller!!!
- Also there can be allowed boubds yah, 
- On the right usually as long bigger than the lower bound can liao
- On the left usually as long smaller than the upper bound can liao


2. some form of DFs?



4. Usig bottom up dfs for this


# You should be able to do this yah!!
- what do we want??
- We have to both a top down and bootom up apprpach 
- For the top down, we have to pass down the upper and lower limit, which then satisfy the BST for all the sbu trees
- For bottom up, it is from the return at the bottom yah 
- Usally top down we have to create a function to hold things to pass down@!!



"""


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # I need propogate teh root value?
        def dfs(node, lower, upper):

            if not node:
                return True


            if not lower < node.val <upper:
                return False

            left = dfs(node.left, lower, node.val)
            right = dfs(node.right, node.val, upper)

            return left and right

        return dfs(root, float('-inf'), float('inf'))


