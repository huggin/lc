class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        row = [[0] * 10 for _ in range(9)]
        col = [[0] * 10 for _ in range(9)]
        box = [[0] * 10 for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    d = ord(board[i][j]) - ord("0")
                    row[i][d] = 1
                    col[j][d] = 1
                    box[i // 3 * 3 + j // 3][d] = 1

        def dfs(i, j):
            if i == 9:
                return True
            if j == 9:
                return dfs(i + 1, 0)

            if board[i][j] != ".":
                return dfs(i, j + 1)

            for k in range(1, 10):
                ok = row[i][k] + col[j][k] + box[i // 3 * 3 + j // 3][k]
                if ok == 0:
                    row[i][k] = 1
                    col[j][k] = 1
                    box[i // 3 * 3 + j // 3][k] = 1
                    board[i][j] = chr(ord("0") + k)
                    if dfs(i, j + 1):
                        return True
                    board[i][j] = "."
                    row[i][k] = 0
                    col[j][k] = 0
                    box[i // 3 * 3 + j // 3][k] = 0
            return False

        dfs(0, 0)
