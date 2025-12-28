class Solution:
    def countUnguarded(
        self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]
    ) -> int:
        ans = 0
        matrix = [[0] * n for _ in range(m)]
        for i, j in guards:
            matrix[i][j] = 1
        for i, j in walls:
            matrix[i][j] = 2
        for i, j in guards:
            x, y = i - 1, j
            while x >= 0 and matrix[x][y] != 1 and matrix[x][y] != 2:
                matrix[x][y] = 3
                x -= 1
            x = i + 1
            while x < m and matrix[x][y] != 1 and matrix[x][y] != 2:
                matrix[x][y] = 3
                x += 1
            x, y = i, j - 1
            while y >= 0 and matrix[x][y] != 1 and matrix[x][y] != 2:
                matrix[x][y] = 3
                y -= 1
            y = j + 1
            while y < n and matrix[x][y] != 1 and matrix[x][y] != 2:
                matrix[x][y] = 3
                y += 1
        for row in matrix:
            for cell in row:
                if cell == 0:
                    ans += 1
        return ans
