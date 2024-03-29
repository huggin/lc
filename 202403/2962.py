class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ma = max(nums)
        cnt = 0
        ans = 0
        n = len(nums)
        j = 0
        for i in range(n):
            if nums[i] == ma:
                cnt += 1
            while cnt >= k:
                ans += n - i
                if nums[j] == ma:
                    cnt -= 1
                j += 1
        return ans
