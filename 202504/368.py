class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [1] * n
        prev = [-1] * n
        ma = -1
        pos = -1
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        prev[i] = j
            if dp[i] > ma:
                ma = dp[i]
                pos = i

        ans = []
        while pos != -1:
            ans.append(nums[pos])
            pos = prev[pos]
        return ans
