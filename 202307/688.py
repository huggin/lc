class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dx = [-2, -2, -1, -1, 1, 1, 2, 2]
        dy = [-1, 1, -2, 2, -2, 2, -1, 1]
        q = deque()
        q.append((row * n + column, 1))

        for _ in range(k):
            d = defaultdict(int)
            while q:
                key, prob = q.popleft()
                x = key // n
                y = key % n
                for i in range(8):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx >= 0 and nx < n and ny >= 0 and ny < n:
                        d[nx * n + ny] += prob / 8

            for key, v in d.items():
                q.append((key, v))

        ans = 0.0
        while q:
            _, prob = q.popleft()
            ans += prob
        return ans
