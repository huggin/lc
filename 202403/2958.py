class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        j = 0
        ans = 0
        n = len(nums)
        for i in range(n):
            d[nums[i]] += 1
            while d[nums[i]] > k:
                d[nums[j]] -= 1
                j += 1
            ans = max(ans, i - j + 1)
        return ans
