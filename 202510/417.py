class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        po = []
        ao = []
        q = deque()
        n = len(heights)
        m = len(heights[0])
        vis = [[0] * m for _ in range(n)]
        for i in range(n):
            q.append((i, 0))
            vis[i][0] = 1
        for i in range(1, m):
            q.append((0, i))
            vis[0][i] = 1
        dx = [-1, 0, 0, 1]
        dy = [0, -1, 1, 0]
        while q:
            i, j = q.popleft()
            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]
                if 0 <= ni < n and 0 <= nj < m and vis[ni][nj] == 0 and heights[ni][nj] >= heights[i][j]:
                    vis[ni][nj] = 1
                    q.append((ni, nj))

        for i in range(n):
            q.append((i, m-1))
            vis[i][m-1] |= 2
        for i in range(m-1):
            q.append((n-1, i))
            vis[n-1][i] |= 2
        while q:
            i, j = q.popleft()
            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]
                if 0 <= ni < n and 0 <= nj < m and (vis[ni][nj] & 2) == 0 and heights[ni][nj] >= heights[i][j]:
                    vis[ni][nj] |= 2
                    q.append((ni, nj))
        ans = []
        for i in range(n):
            for j in range(m):
                if vis[i][j] == 3:
                    ans.append([i, j])
        return ans

