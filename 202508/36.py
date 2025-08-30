class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = [0] * 10
            for j in range(9):
                if board[i][j] != '.':
                    row[ord(board[i][j]) - ord('0')] += 1
            for j in range(10):
                if row[j] > 1:
                    return False
        
        for i in range(9):
            col = [0] * 10
            for j in range(9):
                if board[j][i] != '.':
                    col[ord(board[j][i]) - ord('0')] += 1
            for j in range(10):
                if col[j] > 1:
                    return False
        
        for i in range(0, 3):
            for j in range(0, 3):
                cnt = [0] * 10
                for i2 in range(i * 3, i * 3 + 3):
                    for j2 in range(j * 3, j * 3 + 3):
                        if board[i2][j2] != '.':
                            cnt[ord(board[i2][j2]) - ord('0')] += 1
                for k in range(10):
                    if cnt[k] > 1:
                        return False
        return True
