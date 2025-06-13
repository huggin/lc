class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        n = len(nums)
        nums.sort()

        def ok(u):
            i = 1
            cnt = 0
            while i < n:
                if nums[i] - nums[i - 1] <= u:
                    cnt += 1
                    i += 2
                else:
                    i += 1
            return cnt >= p

        ans = -1
        lo, hi = 0, max(nums) - min(nums)
        while lo <= hi:
            mi = lo + hi >> 1
            if ok(mi):
                ans = mi
                hi = mi - 1
            else:
                lo = mi + 1
        return ans
