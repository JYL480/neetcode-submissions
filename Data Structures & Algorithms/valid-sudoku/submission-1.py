"""
0. Urm, we just have to use hashset() using default list. 
Then we can aslo know the quadrants as wel l

1. Return a boolean. Check the rows, col and the squares have only numerical unique numbers

Im just going to skip yeah


"""


from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_hash = defaultdict(set)
        col_hash = defaultdict(set)
        sq_hash = defaultdict(set)

        for r in range(9):
            for c in range(9):
                value = board[r][c]

                sq_cor = ((r//3, c//3))

                if value == ".":
                    continue

                # Do the checks here?
                if value in row_hash[r] or value in col_hash[c] or value in sq_hash[sq_cor]:
                    return False

                # Then here I will pop?
                row_hash[r].add(value)
                col_hash[c].add(value)
                sq_hash[sq_cor].add(value)
                
                print(row_hash)

        return True
            





        