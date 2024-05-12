class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        ans = [[0 for _ in range(n - 2)] for _ in range(n - 2)]
        for i in range(n - 2):
            for j in range(n - 2):
                temp = grid[i][j]
                for k in range(i, i + 3):
                    for l in range(j, j + 3):
                        temp = max(temp, grid[k][l])
                ans[i][j] = temp
        return ans
