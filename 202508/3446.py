class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        for k in range(-n+1, n):
            a = []
            if k < 0:
                for i in range(n+k):
                    a.append(grid[i][i-k])
                a.sort()
                j = 0
                for i in range(n+k):
                    grid[i][i-k] = a[j]
                    j += 1
            else:
                for j in range(n-k):
                    a.append(grid[j+k][j])
                a.sort()
                i = len(a) - 1
                for j in range(n-k):
                    grid[j+k][j] = a[i]
                    i -= 1
                    
        return grid
