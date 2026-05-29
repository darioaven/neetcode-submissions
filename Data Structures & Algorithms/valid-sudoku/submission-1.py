from collections import Counter
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_d = [Counter() for _ in range(9)] 
        col_d = [Counter() for _ in range(9)]
        sqr_d = [Counter() for _ in range(9)] 

        for i in range(9):
            for j in range(9):
                ind = board[i][j]
                if ind == ".":
                    continue
                ind = int(ind)
                
                sqr_ind = 3 * (i//3) + j//3

                row_d[i][ind] += 1
                col_d[j][ind] += 1
                sqr_d[sqr_ind][ind] += 1
                
                if row_d[i][ind] > 1 or col_d[j][ind] > 1 or sqr_d[sqr_ind][ind] > 1:
                    return False

        return True

        