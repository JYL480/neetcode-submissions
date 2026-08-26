# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
0. What is inversiion
- You want to see the sub tree, go to all the nodes available then you will swap the child
- We can usse DFS for this? 
- We can use recursion yah

"""

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # This
        if not root:
            return 


        # how do you swap the children?
        tmp = root.left
        root.left = root.right
        root.right = tmp 

        self.invertTree(root.left)

        self.invertTree(root.right)


        return root