class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        d = {}
        ans = -1

        def f(a):
            ans = 0
            while a > 0:
                ans += a % 10
                a //= 10
            return ans

        for c in nums:
            dv = f(c)
            if dv in d:
                ans = max(ans, d[dv] + c)
                d[dv] = max(d[dv], c)
            else:
                d[dv] = c
        return ans
