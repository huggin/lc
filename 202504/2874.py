class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ans = 0
        ma = nums[0]
        n = len(nums)
        delta = 0
        for i in range(1, n):
            ans = max(ans, delta * nums[i])
            delta = max(delta, ma - nums[i])
            ma = max(ma, nums[i])
        return ans
