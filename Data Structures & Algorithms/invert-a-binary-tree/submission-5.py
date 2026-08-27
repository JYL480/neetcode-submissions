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

timie = O(N) becos you only visit the node onces only yah 
-  Space = O(W) widuth of thiss shit best casse is if its a isngle line space = O(1) ebcauuse eahc laevel youare sotring only 1 node
- worst case = N + 1/2 or O(N)



"""


from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Lets try with the recursion yag?
        # we need an ednding condito?
        if not root:
            return

        # This is waht idk

        root.left , root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root



