class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        presum = [0]
        for a in nums:
            presum.append(presum[-1] + a)
        
        dp = [[0 for _ in range(4)] for _ in range(n+1)]
        ans = [[[] for _ in range(4)] for _ in range(n+1)]
        for i in range(k, n+1):
            for j in range(1, 4):
                if dp[i-1][j] < dp[i-k][j-1] + presum[i] - presum[i-k]:
                    dp[i][j] = dp[i-k][j-1] + presum[i] - presum[i-k]
                    ans[i][j] = ans[i-k][j-1].copy()
                    ans[i][j].append(i-k)
                else:
                    dp[i][j] = dp[i-1][j]
                    ans[i][j] = ans[i-1][j].copy()
        
        return ans[n][3]
