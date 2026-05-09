class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        def f(x1, y1, x2, y2):
            a = []
            x, y = x1, y1
            a.append(grid[x][y])
            y += 1
            i = 0
            while not (x == x1 and y == y1):
                a.append(grid[x][y])
                nx = x + dx[i]
                ny = y + dy[i]
                if not (x1 <= nx <= x2 and y1 <= ny <= y2):
                    i += 1
                    nx = x + dx[i]
                    ny = y + dy[i]
                x, y = nx, ny
            n = len(a)
            k1 = k % n
            a = a[k1:] + a[:k1]
            j = 0
            i = 0
            while j < n:
                grid[x][y] = a[j]
                j += 1
                nx = x + dx[i]
                ny = y + dy[i]
                if not (x1 <= nx <= x2 and y1 <= ny <= y2):
                    i += 1
                    nx = x + dx[i]
                    ny = y + dy[i]
                x, y = nx, ny

        x1, y1 = 0, 0
        x2, y2 = len(grid) - 1, len(grid[0]) - 1
        while x1 < x2 and y1 < y2:
            f(x1, y1, x2, y2)
            x1 += 1
            x2 -= 1
            y1 += 1
            y2 -= 1
        return grid
