# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
0. Now wtf is this, 


1. WHat do they want?
- They want to count good nodes in the binary tree?
- Meaing how many nodes are the biggest within the path!
- And it contains root itsef, because it snot bigger than itself?


2. edge cases? Im very tired bruh. Cant think...


4. What kind of pattern is this?
- How would  my current node know that im larger, urmm i needd to know from my parents
- So this would be a top down solution with DFS
- Commonly a top down DFS will be in the pre order yah
- You pass and then check? whther the rucrrent node is large or not?


"""
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        res = 0
        maxvalue = 0
        def dfs(node, maxvalue):

            if not node:
                return 0 # We will return 0 value

            # I will process first yah 
            if node.val >= maxvalue:
                res = 1
            else:
                res = 0 
            
            maxvalue = max(node.val, maxvalue)
            

            res += dfs(node.left, maxvalue)
            res += dfs(node.right, maxvalue)

            return res

        return dfs(root, root.val)

            
            






        # def dfs(node, mv):
        #     if not node:
        #         return 0 
        #     res = 1 if node.val >= mv else 0

        #     mv = max(mv, node.val) # Info from parents to child!!!! We can child needs info from the parents!
            
        #     #PRE ORDER travelr
        #     res += dfs(node.left, mv)
        #     res += dfs(node.right, mv)

        #     return res
        # return dfs(root, root.val)