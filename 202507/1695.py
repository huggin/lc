class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        tt = 0
        s = set()
        j = 0
        n = len(nums)
        ans = 0
        for i in range(n):
            if nums[i] in s:
                while j < i and nums[j] != nums[i]:
                    tt -= nums[j]
                    s.remove(nums[j])
                    j += 1
                tt -= nums[j]
                s.remove(nums[j])
                j += 1
            tt += nums[i]
            ans = max(tt, ans)
            s.add(nums[i])
        return ans
