# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
0.  This is DFS recursion ts yah
- Rmb your base case will be the one changing, how do we do this in the BFS idk 

1. What do they want?
- They want to return Bool value, true or false ,whether in there is subtree in teh root that contains
- that is equal to the sub root!!

2. What is the naive solution IDK
- Brute force and cehck one by one


3. Bottle neck?
- O(NM)? for timecomeplecity

4. Proper solution
- We will create a subfunction which calls to check if its the same tree
- so the funciton above plus some recursion!!


5. Time compelxit 
Time: O(NM) Will go trhough all the main root node once and the other
space: O(1)

6. Yeah forgot baout the edge cases?
- If null and normal 
- If both null


- Okay I will retry
- We have to search to all the roots then do the is subtree
- And in the sameTree to check we need to recusrively check the sub nodes!!
- We have 2 separate recusrive function yah


"""

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # OKay thatn we have to go to each root yah
        # But we also have to do the edge cases!!
        if root and not subRoot: # meaning sr is not null ,it iwll alway sbe sr of root
            return True

        if not root:
            return False

        if self.sameTree(root, subRoot):
            return True

        # Then we move on recursive to the next

        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        return left or right


    def sameTree(self, r, s):
        if not r and not s:
            return True

        elif not r or not s:
            return False

        elif r.val != s.val:
            return False

        return self.sameTree(r.left, s.left) and self.sameTree(r.right, s.right) 
            
        




        
        