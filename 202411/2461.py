class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        cnt = [0] * (max(nums) + 1)
        unique = 0
        total = 0
        for i in range(k):
            total += nums[i]
            cnt[nums[i]] += 1
            if cnt[nums[i]] == 1:
                unique += 1

        if unique == k:
            ans = max(ans, total)

        for i in range(k, n):
            total -= nums[i - k]
            total += nums[i]
            cnt[nums[i - k]] -= 1
            if cnt[nums[i - k]] == 0:
                unique -= 1
            cnt[nums[i]] += 1
            if cnt[nums[i]] == 1:
                unique += 1
            if unique == k:
                ans = max(ans, total)

        return ans
