# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
0. Okay how would you do this?
- for a same binary question?
- Note that this question is do from the ground up yah
- Meaning what?
- What can be compared? - This based condition is what?
- base condition is the comparison to return true or false

4. So this is ground up recusrion
- THis is some recusrive function yah to solve this problem

- We need to do some recurrsive function for thiss

- OKAY when we are referring to the base case, we mean the very end, meaning it will only return when we are on the last leg ts!!

- So once we base case means to reach down to the very end yah!!!!

"""


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: # both are null, this is truee
            return True

        elif not p or not q: # either 1 is null , then its false
            return False

        elif  p.val != q.val:
            return False


        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

        return left and right
        
        