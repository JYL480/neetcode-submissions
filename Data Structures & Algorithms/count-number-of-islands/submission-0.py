"""
0. Prob use some search, DFS or BFS
to search and do some recursion!!! Which is in a way youre doing DFS I think 
DFS - 3 things
BFS - 1 thing

1. They want to count the number of islands yah!!!
Return an integer

2. 

4. Pattern
- We will call some recursion DFS 
- we will do a nested for loop
 
dfs(r_index, c_index)
    # we need some stopping
    # outside the grid or something
    # we weill return if we visted or water
    # WE need to mark whehter we visited, if not there be overlaps



    if we hit a 1. then we will index the up donw left right 
    dfs(r, c - 1) l
    dfs(r, c + 1) r
    dfs(r -1 , c) u
    dfs(r + 1, c) d

Outside

def ....

    nested for loop for this yah


    for r in rows:
        for c in cols:
            if grid[r][c] ==1:
                count +=1
                dfs

"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            # we need to have ending fucntisn yah

            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            if grid[r][c] == "0":
                return 
            
            else:
                grid[r][c] = "0" # We will mark visited

            
            dfs(r -1 , c) # up 
            dfs(r +1 , c) # down
            dfs(r , c - 1) # left
            dfs(r , c + 1) # right

        count = 0
        # we wil go rhtourhg each etnry then 
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1
                    dfs(r, c)
        return count






