class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        v = [0] * (n * n + 1)
        for row in grid:
            for item in row:
                v[item] += 1

        ans = [-1, -1]
        for i in range(1, n * n + 1):
            if v[i] == 2:
                ans[0] = i
            elif v[i] == 0:
                ans[1] = i
        return ans
