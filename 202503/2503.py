class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        q = [(v, k) for k, v in enumerate(queries)]
        q.sort()
        dx = [-1, 0, 0, 1]
        dy = [0, -1, 1, 0]
        n = len(grid)
        m = len(grid[0])
        v = [[0] * m for _ in range(n)]
        ql = len(q)
        ans = [0] * ql
        pq = []

        j = bisect.bisect(q, (grid[0][0], ql))
        if j < ql:
            ans[q[j][1]] += 1
            heapq.heappush(pq, (grid[0][0], 0, 0, j))
        v[0][0] = 1

        while len(pq) > 0:
            curr, x, y, prev = heapq.heappop(pq)
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if nx >= 0 and nx < n and ny >= 0 and ny < m and v[nx][ny] == 0:
                    v[nx][ny] += 1
                    j = bisect.bisect(q, (grid[nx][ny], ql), lo=prev)
                    if j != ql:
                        ans[q[j][1]] += 1
                        heapq.heappush(pq, (grid[nx][ny], nx, ny, j))

        for i in range(1, ql):
            ans[q[i][1]] += ans[q[i - 1][1]]
        return ans
