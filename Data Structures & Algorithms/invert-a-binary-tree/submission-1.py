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
        # We can use the iterative DFS pre and post order
        if not root:
            return None

        stack = [root]

        while stack:
            node = stack.pop()
            tmp = node.left  
            node.left = node.right
            node.right = tmp 

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return root
