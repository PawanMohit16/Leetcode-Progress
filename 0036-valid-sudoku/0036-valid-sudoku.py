class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r = len(board)
        c = len(board[0])

        row_s = collections.defaultdict(set)
        col_s = collections.defaultdict(set)
        nine_s = collections.defaultdict(set)


        for i in range(r):
            for j in range(c):
                if board[i][j] != '.':
                    if board[i][j] in row_s[i] or board[i][j] in col_s[j] or board[i][j] in nine_s[(i // 3, j // 3)]:
                        return False
                    
                    row_s[i].add(board[i][j])
                    col_s[j].add(board[i][j])
                    nine_s[i // 3, j // 3].add(board[i][j])

            

        return True


        