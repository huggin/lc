class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ps_row = [[0] for _ in range(m)]
        ps_col = [[0] for _ in range(n)]
        for i in range(m):
            for j in range(n):
                ps_row[i].append(ps_row[i][-1] + grid[i][j])
                ps_col[j].append(ps_col[j][-1] + grid[i][j])

        d1, d2 = {}, {}

        def add(x, y):
            idx = x - y
            d1[idx] = [0]
            while 0 <= x < m and 0 <= y < n:
                d1[idx].append(d1[idx][-1] + grid[x][y])
                x, y = x + 1, y + 1

        def add2(x, y):
            idx = x + y
            d2[idx] = [0]
            while 0 <= x < m and 0 <= y < n:
                d2[idx].append(d2[idx][-1] + grid[x][y])
                x, y = x + 1, y - 1

        for y in range(n):
            add(0, y)
            add2(0, y)
        for x in range(1, m):
            add(x, 0)
            add2(x, n - 1)

        for k in range(min(m, n), 1, -1):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    found = True
                    v = ps_row[i][j + k] - ps_row[i][j]
                    for ii in range(i + 1, i + k):
                        if ps_row[ii][j + k] - ps_row[ii][j] != v:
                            found = False
                            break
                    if not found:
                        continue
                    for ii in range(j, j + k):
                        if ps_col[ii][i + k] - ps_col[ii][i] != v:
                            found = False
                            break
                    if not found:
                        continue
                    ii = min(i, j)
                    jj = min(i, n - 1 - (j + k - 1))
                    if d1[i - j][ii + k] - d1[i - j][ii] != v:
                        continue
                    if d2[i + j + k - 1][jj + k] - d2[i + j + k - 1][jj] != v:
                        continue
                    return k
        return 1
