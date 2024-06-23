class MQ:
    def __init__(self, arr=None, ismax=True):
        self.ismax = ismax
        self.q = deque()
        self.m = deque()
        if arr is not None:
            for val in arr:
                self.push(val)

    def push(self, val):
        self.q.append(val)
        if self.ismax:
            while self.m and self.m[-1] < val:
                self.m.pop()
        else:
            while self.m and self.m[-1] > val:
                self.m.pop()
        self.m.append(val)

    def pop(self):
        assert self.q
        if self.q[0] == self.m[0]:
            self.m.popleft()
        self.q.popleft()

    def get(self):
        INF = float("inf")
        if not self.m:
            return -INF if self.ismax else INF
        return self.m[0]

    def size(self):
        return len(self.q)


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        mq1 = MQ(ismax=True)
        mq2 = MQ(ismax=False)
        ans = 1
        j = 0
        for a in nums:
            mq1.push(a)
            mq2.push(a)
            while mq1.get() - mq2.get() > limit:
                mq1.pop()
                mq2.pop()
            ans = max(ans, mq1.size())
        return ans
