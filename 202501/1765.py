class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        q = deque()
        m = len(isWater)
        n = len(isWater[0])
        ans = [[-1] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    q.append((i, j))
                    ans[i][j] = 0

        dx = [-1, 0, 0, 1]
        dy = [0, -1, 1, 0]
        while q:
            sz = len(q)
            for _ in range(sz):
                i, j = q.popleft()
                for k in range(4):
                    ni = i + dx[k]
                    nj = j + dy[k]
                    if ni >= 0 and ni < m and nj >= 0 and nj < n and ans[ni][nj] == -1:
                        ans[ni][nj] = ans[i][j] + 1
                        q.append((ni, nj))
        return ans
