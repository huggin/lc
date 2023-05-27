import bisect


class Solution:
    def query(self, idx):
        ans = 0
        idx += 1
        while idx > 0:
            ans = max(ans, self.bit[idx])
            idx -= idx & -idx
        return ans

    def update(self, idx, val):
        idx += 1
        while idx < self.n:
            self.bit[idx] = max(val, self.bit[idx])
            idx += idx & -idx

    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        a = sorted(obstacles)
        n = len(obstacles)
        for i in range(n):
            idx = bisect.bisect_left(a, obstacles[i])
            obstacles[i] = idx

        self.bit = [0] * (n + 1)
        self.n = n + 1
        ans = []
        for o in obstacles:
            d = self.query(o) + 1
            ans.append(d)
            self.update(o, d)

        return ans
