from collections import deque


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        marked = n * [0]
        ans = 0
        q = deque()
        for i in range(n):
            if marked[i] == 0:
                ans += 1
                q.append(i)
                marked[i] = 1
                while q:
                    v = q.popleft()
                    for w in range(n):
                        if isConnected[v][w] == 1 and marked[w] == 0:
                            q.append(w)
                            marked[w] = 1

        return ans
