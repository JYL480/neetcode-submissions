# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
0. My first intuition is that a bottom up apporach
- But the answer will only be known at the end 
- At the very end or in the mmiddle???????
- Or it can be both the return + update the outside global state 

4. Woah how would I do this???
- I can have node1left, node2left and so on and then vompare the value 
- I think ththis will be bottom up as well!!!!!!!


"""


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # So what matters in this question are the base cases!!!
        # Cause only at the base cases is where you will compare the nodes yah
        # THis means you need to see  Null 
        # both empty
        if not p and not q:
            return True

        # one empty, one not empty
        if not p or not q or p.val != q.val:
            return False


        
        # check children
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

        return left and right

        