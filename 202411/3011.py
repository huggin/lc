class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        def countBit(x):
            cnt = 0
            while x > 0:
                cnt += 1
                x &= x - 1
            return cnt

        a = list(map(countBit, nums))
        n = len(a)
        prev = -1
        mi = nums[0]
        ma = nums[0]
        i = 1
        while i < n:
            if a[i] != a[i - 1]:
                prev = ma
                mi = nums[i]
                ma = nums[i]
                if mi < prev:
                    return False
            else:
                mi = min(mi, nums[i])
                ma = max(ma, nums[i])
                if mi < prev:
                    return False
            i += 1

        return True
