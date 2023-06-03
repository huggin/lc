from collections import deque


class Solution:
    def numOfMinutes(
        self, n: int, headID: int, manager: List[int], informTime: List[int]
    ) -> int:
        tree = [[] for _ in range(n)]
        q = deque()
        for i in range(n):
            if manager[i] == -1:
                q.append(i)
            else:
                tree[manager[i]].append(i)

        time = [0] * n
        ans = 0
        while q:
            v = q.popleft()
            ans = max(ans, time[v])
            for w in tree[v]:
                time[w] = time[v] + informTime[v]
                q.append(w)

        return ans
