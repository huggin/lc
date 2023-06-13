class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        d = {}
        n = len(grid)
        p = 100003
        m = int(1e9 + 7)
        for i in range(n):
            hash = 0
            for j in range(n):
                hash = (hash * p + grid[i][j]) % m
            if hash in d:
                d[hash] += 1
            else:
                d[hash] = 1

        ans = 0
        for i in range(n):
            hash = 0
            for j in range(n):
                hash = (hash * p + grid[j][i]) % m

            if hash in d:
                ans += d[hash]

        return ans
