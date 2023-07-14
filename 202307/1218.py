class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n = len(arr)
        dp = defaultdict(int)
        ans = 1
        for i in range(n):
            dp[arr[i]] = max(dp[arr[i] - difference] + 1, dp[arr[i]])
            ans = max(ans, dp[arr[i]])
        return ans
