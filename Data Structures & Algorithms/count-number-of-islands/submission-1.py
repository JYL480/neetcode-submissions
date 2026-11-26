"""
0. Numbe od islands!
- THis will have to some DFS recursion thingy loh.
- in your dfs function you will need to have ending function yah and some boundaries....



4. 

dfs(r - 1, c) # up 
dfs(r + 1, c) # down
dfs(r, c - 1) #left
dfs(r, c + 1) # right

"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        n_rows = len(grid)
        n_cols = len(grid[0])
        
        def dfs(r, c): # Passing 0 indexing yah 
            # You need to indicate your ending condition
            if r < 0 or r >= n_rows or c < 0 or c >= n_cols :
                return 

            # Okay then when you have reached a nothing or water
            if grid[r][c] == "0":
                return 

            else:
                grid[r][c] = "0" # Will make as visited

            dfs(r - 1, c) # up 
            dfs(r + 1, c) # down
            dfs(r, c - 1) #left
            dfs(r, c + 1) # right

            # Call this recusrively loh


        # Then the ouside will go through with a nest for lloop
        count = 0 
        for r in range(n_rows):
            for c in range(n_cols):
                if grid[r][c] == "1":
                    count += 1
                    dfs(r, c)

        return count