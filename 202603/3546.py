class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        tt = 0
        for row in grid:
            for item in row:
                tt += item
        m = len(grid)
        n = len(grid[0])
        curr = 0
        for row in grid:
            for item in row:
                curr += item
            if curr + curr == tt:
                return True
        curr = 0
        for i in range(n):
            for j in range(m):
                curr += grid[j][i]
            if curr + curr == tt:
                return True
        return False
