"""
0. what is this, they want us to find all possible combinations of things below
- Return the all combinations. We can use backtracking method which involves the use of DFS!! Which allows for undo and etc.....


1. What is 


4. Main ideas
Choose explore undo (backtrack) it will be in a decision treeAll of b

"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        path = []

        def dfs(i): # i here will be doing the indexing
            
            # WHen workign with dfs there has to be an ending condition
            if (i == len(nums)): # Meaning we have reached the end, we then return
                res.append(path.copy()) 
                return

            # First include 
            path.append(nums[i])

            dfs(i + 1) # go to the next include

            path.pop()

            dfs(i + 1) # go to nect exlude

        dfs(0)

        return res