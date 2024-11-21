class Solution:
    def countUnguarded(
        self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]
    ) -> int:
        q = deque()
        used = 0
        visit = [[[0 for _ in range(n)] for _ in range(m)] for _ in range(4)]
        for x, y in guards:
            for i in range(4):
                q.append((x, y, i))
                visit[i][x][y] = 1

        for x, y in walls:
            for i in range(4):
                visit[i][x][y] = 1

        dx = [-1, 0, 0, 1]
        dy = [0, -1, 1, 0]

        while q:
            x, y, d = q.popleft()
            if d == -1:
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if (
                        nx >= 0
                        and nx < m
                        and ny >= 0
                        and ny < n
                        and visit[i][nx][ny] == 0
                    ):
                        visit[i][nx][ny] = 1
                        q.append((nx, ny, i))
            else:
                nx = x + dx[d]
                ny = y + dy[d]

                if nx >= 0 and nx < m and ny >= 0 and ny < n and visit[d][nx][ny] == 0:
                    visit[d][nx][ny] = 1
                    q.append((nx, ny, d))

        ans = 0
        for i in range(m):
            for j in range(n):
                found = True
                for k in range(4):
                    if visit[k][i][j]:
                        found = False
                        break
                if found:
                    ans += 1
        return ans
