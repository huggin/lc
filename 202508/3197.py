class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        @cache
        def calc(x1, y1, x2, y2):
            i1, i2 = n, 0
            j1, j2 = m, 0
            for i in range(x1, x2+1):
                for j in range(y1, y2+1):
                    if grid[i][j]:
                        j1 = min(j1, j)
                        j2 = max(j2, j)
                        i1 = min(i1, i)
                        i2 = max(i2, i)
            return (j2 - j1 + 1) * (i2 - i1 + 1)


        ans = m * n
        for i in range(n-2):
            for j in range(i+1, n-1):
                ans = min(ans, calc(0, 0, i, m-1) + calc(i+1, 0, j, m-1) + calc(j+1, 0, n-1, m-1))
    
        for i in range(m-2):
            for j in range(i+1, m-1):
                ans = min(ans, calc(0, 0, n-1, i) + calc(0, i+1, n-1, j) + calc(0, j+1, n-1, m-1))
        
        for i in range(n-1):
            for j in range(m-1):
                ans = min(ans, calc(0, 0, i, m-1) + calc(i+1, 0, n-1, j) + calc(i+1, j+1, n-1, m-1))
                ans = min(ans, calc(i+1, 0, n-1, m-1) + calc(0, 0, i, j) + calc(0, j+1, i, m-1))
                ans = min(ans, calc(0, 0, n-1, j) + calc(0, j+1, i, m-1) + calc(i+1, j+1, n-1, m-1))
                ans = min(ans, calc(0, j+1, n-1, m-1) + calc(0, 0, i, j) + calc(i+1, 0, n-1, j))

        return ans

