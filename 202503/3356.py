class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        m = len(queries)

        def ok(j):
            ps = [0] * (n + 1)
            for i in range(j):
                ps[queries[i][0]] += queries[i][2]
                ps[queries[i][1] + 1] -= queries[i][2]
            for i in range(1, n + 1):
                ps[i] += ps[i - 1]
            for i in range(n):
                if ps[i] < nums[i]:
                    return False
            return True

        ans = -1
        lo, hi = 0, m
        while lo <= hi:
            mi = lo + hi >> 1
            if ok(mi):
                ans = mi
                hi = mi - 1
            else:
                lo = mi + 1

        return ans
