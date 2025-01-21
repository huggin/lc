import math


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        ps = [[0] for _ in range(2)]
        for i in range(2):
            for a in grid[i]:
                ps[i].append(ps[i][-1] + a)

        n = len(grid[0])
        ans = math.inf
        for i in range(n):
            ans = min(ans, max(ps[1][i], ps[0][n] - ps[0][i + 1]))
        return ans
