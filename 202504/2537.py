class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        j = 0
        d = {}
        curr = 0
        ans = 0
        for i in range(n):
            if nums[i] in d:
                curr += d[nums[i]]
            
            d[nums[i]] = d.get(nums[i], 0) + 1
            
            while curr >= k:
                ans += n - i
                curr -= d[nums[j]] - 1
                d[nums[j]] -= 1
                j += 1
        return ans
            
