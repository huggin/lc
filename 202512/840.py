class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        def good(i, j):
            a = [grid[k][l] for k in range(i, i+3) for l in range(j, j+3)]
            if sorted(a) != [1,2,3,4,5,6,7,8,9]:
                return False
            for k in range(i, i+3):
                if sum(grid[i][j:j+3]) != 15:
                    return False
            for k in range(j, j+3):
                tot = 0
                for l in range(i, i+3):
                    tot += grid[l][k]

                if tot != 15:
                    return False
            if grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2] != 15:
                return False
            if grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j] != 15:
                return False
            return True

        ans = 0
        for i in range(n-2):
            for j in range(m-2):
                if good(i, j):
                    ans += 1
        return ans    
