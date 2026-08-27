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


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
            # Noew lets try the iterative version yah!! Which is waht? Idk I want to KMS HORRRRASDJDAS:JLKJK:LDSA:JKLDSKLJSDLJK

        stack = [root]

        if not root:
            return None

        # I think i add inside

        # Isiti?

        while stack:
            node = stack.pop()

            node.left , node.right = node.right, node.left

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return root


