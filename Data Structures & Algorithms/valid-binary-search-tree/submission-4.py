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


"""


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # I need propogate teh root value?

        def dfs(root, lower, upper):

            if not root:
                return True

            if not (lower<root.val<upper):
                return False # We want to keep checking, oh we dont want to return so fast, we want to keep seraching 

            
            

            left = dfs(root.left, lower , root.val)
            right = dfs(root.right, root.val,upper )

            # This is the post order shit here
            return left and right

        return dfs(root, float('-inf'), float('inf'))

