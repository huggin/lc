class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums

        n = len(nums)
        if k * 2 >= n:
            return n * [-1]

        ans = n * [-1]
        sum = 0
        for i in range(2 * k + 1):
            sum += nums[i]

        ans[k] = sum // (2 * k + 1)
        for i in range(k + 1, n - k):
            sum = sum - nums[i - k - 1] + nums[i + k]
            ans[i] = sum // (2 * k + 1)
        return ans
