class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        pq = []
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                pq.append(grid[i][j])

        for i in range(m):
            for j in range(n):
                for k in range(1, min((m + 1) // 2, (n + 1) // 2)):
                    if i - k >= 0 and i + k < m and j + 2 * k < n:
                        total = (
                            grid[i][j]
                            + grid[i][j + 2 * k]
                            + grid[i + k][j + k]
                            + grid[i - k][j + k]
                        )
                        for kk in range(1, k):
                            total += grid[i - kk][j + kk]
                            total += grid[i + kk][j + kk]
                            total += grid[i - kk][j + 2 * k - kk]
                            total += grid[i + kk][j + 2 * k - kk]
                        pq.append(total)

        return sorted(set(pq), reverse=True)[0:3]
