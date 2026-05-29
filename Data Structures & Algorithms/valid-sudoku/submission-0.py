from collections import Counter
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_d = [Counter() for _ in range(9)] 
        col_d = [Counter() for _ in range(9)]
        sqr_d = [Counter() for _ in range(9)] 

        row_d[0][10] += 1

        for i in range(9):
            for j in range(9):
                ind = board[i][j]
                if ind == ".":
                    continue
                ind = int(ind)
                 # block logic

                if j < 3:
                    ind2 = 0
                elif j < 6:
                    ind2 = 1
                else:
                    ind2 = 2
                
                if i < 3:
                    x = 0
                elif i < 6:
                    x = 1
                else:
                    x = 2
                
                sqr_ind = 3 * x + ind2

                row_d[i][ind] += 1
                col_d[j][ind] += 1
                sqr_d[sqr_ind][ind] += 1

               
                
                if row_d[i][ind] > 1 or col_d[j][ind] > 1 or sqr_d[sqr_ind][ind] > 1:
                    return False

        return True

        