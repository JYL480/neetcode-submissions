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
Time: O(N) Will go trhough all the main root node once
space: O(1)

6. Yeah forgot baout the edge cases?
- If null and normal 
- If both null



"""

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # We will now do the ending condition yah: if subroot is empty, these are the edge cases
        # Then it will alwyas be a sub tree
        if not subRoot:
            return True

        if not root: # root must have somehting yah
            return False

        if self.sameTree(root,subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        


    def sameTree(self, s,t):
        if not s and not t:
            return True

        if s and t and s.val == t.val: # so after this we have to compare the l and r subtree 
            # This will be a recusrve functionto keep checking yah
            left = self.sameTree(s.left, t.left)
            right = self.sameTree(s.right, t.right)

            return left and right # So if this if statement nvr exits then we will be in moving on to the false condition

        if not s or not t:
            return False



             





        
        