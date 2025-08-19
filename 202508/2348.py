class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        ans = 0
        while i < n:
            j = i
            while j < n and nums[j] == 0:
                j += 1
            cnt = j - i
            i = j + 1
            ans += cnt * (cnt + 1) // 2
        return ans
