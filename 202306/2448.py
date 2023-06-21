class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        a = []
        n = len(nums)
        for i in range(n):
            a.append((nums[i], cost[i]))

        a.sort()

        def f(k):
            ans = 0
            for i in range(n):
                ans += abs(a[i][0] - k) * a[i][1]
            return ans

        lo, hi = a[0][0], a[n - 1][0]
        ans = min(f(lo), f(hi))
        while lo <= hi:
            k1 = lo + (hi - lo) // 3
            k2 = hi - (hi - lo) // 3

            v1 = f(k1)
            v2 = f(k2)
            if v1 > v2:
                lo = k1 + 1
                ans = min(ans, v2)
            elif v1 < v2:
                hi = k2 - 1
                ans = min(ans, v1)
            else:
                lo = k1 + 1
                hi = k2 - 1
                ans = min(ans, v1)

        return ans
