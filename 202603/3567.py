class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]
        if k == 1:
            return ans
        for i in range(m - k + 1):
            for j in range(n - k + 1):
                a = []
                for ii in range(i, i + k):
                    for jj in range(j, j + k):
                        a.append(grid[ii][jj])
                a.sort()
                temp = 10 ** 6
                for kk in range(1, len(a)):
                    if a[kk] != a[kk-1]:
                        temp = min(temp, a[kk] - a[kk-1])
                ans[i][j] = temp if temp != 10 ** 6 else 0
        return ans


