import math
from collections import deque


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        r = [c for _, _, c in bombs]
        g = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                d = math.sqrt(
                    (bombs[i][0] - bombs[j][0]) ** 2 + (bombs[i][1] - bombs[j][1]) ** 2
                )
                g[i][j] = d
                g[j][i] = d

        ans = 0
        for i in range(n):
            marked = [0] * n
            marked[i] = 1
            q = deque()
            q.append(i)
            cnt = 0
            while q:
                v = q.popleft()
                cnt += 1
                for j in range(n):
                    if g[v][j] - 1e-6 <= r[v] and marked[j] == 0:
                        marked[j] = 1
                        q.append(j)
            ans = max(ans, cnt)
        return ans
