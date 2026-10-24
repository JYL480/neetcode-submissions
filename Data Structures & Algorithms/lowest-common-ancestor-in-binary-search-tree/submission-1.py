# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
0. What i can immediately think of is....
- That we are doing some traversal
- Would it be I think a DFS will be the best to see which are my parents right. 
- It it make sense
- Then this will be I think will be a top down right
- I will have to pass the parents value to the my child?
- I need to process that my childeren return True first then I know this is my parent?
- Then it would be bottom up approach!!!

1. What do they want?
- They want toreturn the lowest common ancestor???
- which is what
- If both child == the p and q then return the smaller acstor value?
- Wait we want to find a COMMON ancestoor yah 

then we dont have to vist l or r

2. edge cases?

3. Brute force?

4. What is the pattern, Because this is a BST
- We know that it is in 
- If we know it clearly more than we just move the right
if we know it clearly less htan move to the left
- the inbetween will be the ancestor loh

"""

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        curr = root
        while curr:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right

            else: # meaning it is in btetween 
                return curr


    