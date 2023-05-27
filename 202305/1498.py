import bisect


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        M = int(1e9 + 7)
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(n):
            if nums[i] * 2 > target:
                break
            idx = bisect.bisect(nums, target - nums[i], lo=i)
            cnt = idx - i - 1
            ans = (ans + 2**cnt) % M

        return ans
