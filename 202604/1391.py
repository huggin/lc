class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        v = [[0] * n for _ in range(m)]
        v[0][0] = 1
        q = deque()
        dx = [-1, 0, 0, 1]
        dy = [0, -1, 1, 0]
        q.append((0, 0, grid[0][0]))
        while q:
            i, j, d = q.popleft()
            if d == 1:
                if j + 1 < n and v[i][j+1] == 0 and grid[i][j+1] in [1, 3, 5]:
                    v[i][j+1] = 1
                    q.append((i, j+1, grid[i][j+1]))
                if j - 1 >= 0 and v[i][j-1] == 0 and grid[i][j-1] in [1, 4, 6]:
                    v[i][j-1] = 1
                    q.append((i, j-1, grid[i][j-1]))
            elif d == 2:
                if i + 1 < m and v[i+1][j] == 0 and grid[i+1][j] in [2, 5, 6]:
                    v[i+1][j] = 1
                    q.append((i+1, j, grid[i+1][j]))
                if i - 1 >= 0 and v[i-1][j] == 0 and grid[i-1][j] in [2, 3, 4]:
                    v[i-1][j] = 1
                    q.append((i-1, j, grid[i-1][j]))
            elif d == 3:
                if i + 1 < m and v[i+1][j] == 0 and grid[i+1][j] in [2, 5, 6]:
                    v[i+1][j] = 1
                    q.append((i+1, j, grid[i+1][j]))
                if j - 1 >= 0 and v[i][j-1] == 0 and grid[i][j-1] in [1, 4, 6]:
                    v[i][j-1] = 1
                    q.append((i, j-1, grid[i][j-1]))
            elif d == 4:
                if i + 1 < m and v[i+1][j] == 0 and grid[i+1][j] in [2, 5, 6]:
                    v[i+1][j] = 1
                    q.append((i+1, j, grid[i+1][j]))
                if j + 1 < n and v[i][j+1] == 0 and grid[i][j+1] in [1, 3, 5]:
                    v[i][j+1] = 1
                    q.append((i, j+1, grid[i][j+1]))
            elif d == 5:
                if i - 1 >= 0 and v[i-1][j] == 0 and grid[i-1][j] in [2, 3, 4]:
                    v[i-1][j] = 1
                    q.append((i-1, j, grid[i-1][j]))
                if j - 1 >= 0 and v[i][j-1] == 0 and grid[i][j-1] in [1, 4, 6]:
                    v[i][j-1] = 1
                    q.append((i, j-1, grid[i][j-1]))
            else:
                if i - 1 >= 0 and v[i-1][j] == 0 and grid[i-1][j] in [2, 3, 4]:
                    v[i-1][j] = 1
                    q.append((i-1, j, grid[i-1][j]))
                if j + 1 < n and v[i][j+1] == 0 and grid[i][j+1] in [1, 3, 5]:
                    v[i][j+1] = 1
                    q.append((i, j+1, grid[i][j+1]))
        
        return v[m-1][n-1] == 1
