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

- We basiclaly we need to do the stopping condition and.....
- And recursion
- Recusrion usally works until you 
- Top down and bottom up 
What is the differnece 
The former, means you need to pass knowldeg from parent to child
- So you will comopute the info first before visitn children into the hild
- You will call the recursion then.....

- Bottom up - you need to go all the way down first then you will process\

- This is bottom up approach yah
- Becuse you cannot solve at the parent node, you need to know your child is true to be able to solbe



"""


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Just do again for fun yah 
        # How do you see that they ar eht emsae tree?
        if not p and not q:
            return True

        if not q  or not p:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        