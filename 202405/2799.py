class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        tt = len(set(nums))
        cnt = [0] * 2001

        ans = 0
        n = len(nums)
        j = 0
        for i in range(n):
            cnt[nums[i]] += 1
            if cnt[nums[i]] == 1:
                tt -= 1
            while tt == 0:
                ans += n - i
                cnt[nums[j]] -= 1
                if cnt[nums[j]] == 0:
                    tt += 1
                j += 1
        return ans
