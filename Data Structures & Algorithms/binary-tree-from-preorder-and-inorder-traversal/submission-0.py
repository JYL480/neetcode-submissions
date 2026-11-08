# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
0.This seems like it will be very long?? No?
- With have to TreeNode(...) I guess, use the class they have given us!!
- Urmm idk, what does this quetion want??
- Oh construct the OG with the information they have 


"""



class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        in_dict = {}

        for i, value in enumerate(inorder):
            in_dict[value] = i

        
        self.pre_index =0

        def dfs(l, r):
            if l > r:
                return None # Meanign there is only 1 node here 
            
            root_val = preorder[self.pre_index]
            self.pre_index +=1
            mid_index = in_dict[root_val]
            # We will create the tree as well
            root = TreeNode(root_val)
            root.left = dfs(l, mid_index - 1)
            root.right = dfs(mid_index + 1, r)
            return root

        return dfs(0, len(preorder) - 1)

