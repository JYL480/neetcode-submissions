"""
0. Intuition immediateky
    - When we do duplciates, we will use a hash tables
    - Then we do a whlie loop for all 9 sections? 
1. Just have to follow the sudoko rules in both the box and row and column
- If that is true, that we will return true else false 
- There can only be unique numbers from 1 - 9 yah

2. edge cases?
- All emtpy? - Then return true ig. All "."??

3. Naively
    - Will be the check for loop 3 times. Check row, col and square
    Bottleneck: However this will be O(N^3)

4. I will have a hash set for the rows and column
- prob will track in the tuple? such thta key will be the r,c,square with that specific value?


- Better to have seperate 

5. Time complexity?
To populate the set to look thru all the nubers will be O(n^2) aldy



Reflection

"""
from collections import defaultdict
import math
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_hash = defaultdict(set)
        col_hash = defaultdict(set)
        square_hash = defaultdict(set)

        for row in range(9):
            for col in range(9):

                value = board[row][col] #Will do row by row yah
                if value == ".":
                    continue




                sub_square_index = (row//3, col//3) # This makes the most sense 
                print(sub_square_index) 

                                # Now here will be checking the hashes before adding
                if value in row_hash[row] or value in col_hash[col] or value in square_hash[sub_square_index]:
                    return False
                # I will add the things to row or hash
                row_hash[row].add(value)
                col_hash[col].add(value)
                square_hash[sub_square_index].add(value)
                
                

                # print(row_hash)
        return True
            





        