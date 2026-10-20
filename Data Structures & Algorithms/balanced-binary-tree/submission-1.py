# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
0. So this is a bottom up approach which returns + update global state of a bool yah 
- cos the answer can come from sub tree if I am not wrong yah
- So take note of this
- This will def be a reursive prob i think


4. Will be using  recusive prob
- Each root will return the diff between left and righ t
- If it is > 1 then update the bal flag?????
- Then return the max of the left or right Im wrong + 1 to add on to the next node in the height!!!
- HOHOHOHO


5. Complexities
O(N) Because each node will be visted oce
O(N) worst case because of a skewed tree
O(logn) - which is balanced tree

0. we return something else and they want a diff thingy
- So what do we do?
- This is the bottom up appraoch yah 

1. They want you to return true or false boolean
- And see if the node differ in ehight by 1

5. ATime compelexit 
time: o(N) vist all nodes
space: O(1)

"""


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.ans = True

        def dfs(node):
            if not node: # we have to return the height loh
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            if abs(left - right) > 1:
                self.ans = False

            return 1 + max(left, right) # The max will deteremin the heigth of the sub tree loh

        dfs(root)

        return self.ans
            








