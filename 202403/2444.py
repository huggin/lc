class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums)
        ans = 0
        j = 0
        ma, mi = -1, -1
        for i in range(n):
            if nums[i] > maxK or nums[i] < minK:
                mi, ma = -1, -1
                j = i + 1
            if nums[i] == maxK:
                ma = i
            if nums[i] == minK:
                mi = i

            if mi != -1 and ma != -1:
                ans += min(mi, ma) - j + 1
        return ans
