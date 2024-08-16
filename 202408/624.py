class Solution:
    def maxDistance(self, a: List[List[int]]) -> int:
        mi, ma = a[0][0], a[0][-1]
        m = len(a)
        ans = 0
        for i in range(1, m):
            mi1, ma1 = a[i][0], a[i][-1]
            ans = max(ans, ma1 - mi, ma - mi1)
            mi = min(mi, mi1)
            ma = max(ma, ma1)
        return ans
