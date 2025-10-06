class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        group = []
        i2g = {}
        value = {}
        n = len(heights)
        m = len(heights[0])
        visited = [[0] * m for _ in range(n)]
        dx = [-1, 0, 0, 1]
        dy = [0, -1, 1, 0]
        for i in range(n):
            for j in range(m):
                if visited[i][j] == 0:
                    visited[i][j] = 1
                    q = deque()
                    q.append((i, j))
                    ng = []
                    while q:
                        x, y = q.popleft()
                        ng.append((x, y))
                        for k in range(4):
                            nx = x + dx[k]
                            ny = y + dy[k]
                            if nx >= 0 and nx < n and ny >= 0 and ny < m and visited[nx][ny] == 0  and heights[i][j] == heights[nx][ny]:
                                q.append((nx, ny))
                                visited[nx][ny] = 1
                    group.append(ng)
                    value[len(group)-1] = heights[i][j]
                    for x, y in ng:
                        i2g[(x, y)] = len(group) - 1
        
        visited = [-1] * len(group)
        ans = []
        def dfs(k):
            visited[k] = 0
            q = deque()
            for i, j in group[k]:
                if i == 0 or j == 0:
                    visited[k] |= 1
                if i == n -1 or j == m - 1:
                    visited[k] |= 2
                if visited[k] == 3:
                    return
                q.append((i, j))
            while q:
                i, j = q.popleft()
                for kk in range(4):
                    ni = i + dx[kk]
                    nj = j + dy[kk]
                    if ni < 0 or ni >= n or nj < 0 or nj >= m:
                        continue
                    g = i2g[(ni, nj)]
                    if value[k] < value[g]:
                        continue
                    if visited[g] == -1:
                        dfs(g)
                    visited[k] |= visited[g]

        for i in range(len(group)):
            dfs(i)
        
        for i in range(len(group)):
            if visited[i] == 3:
                ans.extend(group[i])
        return ans
