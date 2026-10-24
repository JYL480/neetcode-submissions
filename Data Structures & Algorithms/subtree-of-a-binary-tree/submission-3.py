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
        if root and not subRoot:
            return True

        if not root:
            return False


        # Then we we check by calling ghre 

        if self.sameTree(root, subRoot):
            return True

        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        return left or right # can be tiehr that is correct!


    def sameTree(self, p ,q):
        if not p and not q:
            return True

        if not p or not q:
            return False


        if p.val != q.val:
            return False

        left = self.sameTree(p.left, q.left)
        right = self.sameTree(p.right, q.right)

        return left and right

    #     # So if we have emtpy subroot
    #     if not subRoot:
    #         return True

    #     if not root and subRoot:
    #         return False

    #     # now we ill check for the sameTree of not
    #     if self.sameTree(root, subRoot):
    #         return True

    #     left = self.isSubtree(root.left, subRoot)
    #     right = self.isSubtree(root.right, subRoot)

    #     return left or right

    # def sameTree(self, r, s):
    #     # what is the ending condition if we are the same tree
    #     # To the very end
    #     if not s and not r: # Boht the nodes we are looking at is null
    #         return True
        
    #     if r and s and r.val == s.val:
    #         left = self.sameTree(r.left, s.left)
    #         right = self.sameTree(r.right, s.right)

    #         return left and right

    #     elif not s or not r:
    #         return False
            
        




        
        