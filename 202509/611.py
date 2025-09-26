class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(n):
            if nums[i] == 0:
                continue
            j = i + 1
            k = j + 1
            while j < n:
                while k < n and nums[i] + nums[j] > nums[k]:
                    k += 1
                ans += k - j - 1
                j += 1
        return ans
