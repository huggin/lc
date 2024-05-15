class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque()
        safe = [[-1 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j, 0))
                    safe[i][j] = 0

        dx = [-1, 0, 0, 1]
        dy = [0, -1, 1, 0]
        while len(q) > 0:
            x, y, d = q.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if nx >= 0 and nx < n and ny >= 0 and ny < n and safe[nx][ny] == -1:
                    safe[nx][ny] = d + 1
                    q.append((nx, ny, d + 1))

        def ok(m):
            if safe[0][0] < m or safe[n - 1][n - 1] < m:
                return False
            q = deque()
            q.append((0, 0))
            v = [[0 for _ in range(n)] for _ in range(n)]
            v[0][0] = 1
            while len(q) > 0:
                x, y = q.popleft()
                if x == n - 1 and y == n - 1:
                    return True
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if (
                        nx >= 0
                        and nx < n
                        and ny >= 0
                        and ny < n
                        and v[nx][ny] == 0
                        and safe[nx][ny] >= m
                    ):
                        v[nx][ny] = 1
                        q.append((nx, ny))
            return False

        ans = n + n
        lo, hi = 0, n + n
        while lo <= hi:
            m = (lo + hi) >> 1
            if ok(m):
                ans = m
                lo = m + 1
            else:
                hi = m - 1

        return ans
