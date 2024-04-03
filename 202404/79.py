class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        dx = (-1, 0, 0, 1)
        dy = (0, -1, 1, 0)

        visited = [[0 for _ in range(m)] for _ in range(n)]

        def dfs(i, j, k):
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True

            for l in range(4):
                ni = i + dx[l]
                nj = j + dy[l]
                if ni < 0 or ni >= n or nj < 0 or nj >= m or visited[ni][nj]:
                    continue
                visited[ni][nj] = 1
                if dfs(ni, nj, k + 1):
                    return True
                visited[ni][nj] = 0

            return False

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    visited[i][j] = 1
                    if dfs(i, j, 0):
                        return True
                    visited[i][j] = 0
        return False
