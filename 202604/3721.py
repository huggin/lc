class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.sum = [0] * (self.n * 4)
        self.min = [0] * (self.n * 4)
        self.max = [0] * (self.n * 4)

    def merge(self, i):
        self.sum[i] = self.sum[i * 2] + self.sum[i * 2 + 1]
        self.min[i] = min(self.min[i * 2], self.min[i * 2 + 1] + self.sum[i * 2])
        self.max[i] = max(self.max[i * 2], self.max[i * 2 + 1] + self.sum[i * 2])

    def update(self, pos, val):
        self._update(1, 0, self.n - 1, pos, val)

    def _update(self, v, tl, tr, pos, val):
        if tl == tr:
            self.sum[v] = val
            self.min[v] = val
            self.max[v] = val
            return

        tm = tl + tr >> 1
        if pos <= tm:
            self._update(v * 2, tl, tm, pos, val)
        else:
            self._update(v * 2 + 1, tm + 1, tr, pos, val)
        self.merge(v)

    def _exist(self, v, sb):
        return self.min[v] + sb <= 0 <= self.max[v] + sb

    def query(self, v, tl, tr, current):
        if not self._exist(v, current):
            return -1
        if tl == tr:
            return tl
        tm = tl + tr >> 1
        current2 = current + self.sum[v * 2]
        if self._exist(v * 2 + 1, current2):
            return self.query(v * 2 + 1, tm + 1, tr, current2)
        return self.query(v * 2, tl, tm, current)


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        sgt = SegmentTree(n)
        first = {}
        ans = 0
        for l in range(n - 1, -1, -1):
            if nums[l] in first:
                print(l, nums[l], first[nums[l]])
                sgt.update(first[nums[l]], 0)
            first[nums[l]] = l
            sgt.update(l, 1 if nums[l] % 2 == 0 else -1)
            r = sgt.query(1, 0, sgt.n - 1, 0)
            if r >= l:
                ans = max(ans, r - l + 1)
        return ans
