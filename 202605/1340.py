class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        dp = [-1] * n
        def f(k):
            if dp[k] != -1:
                return dp[k]
            j = k - 1
            ans = 1
            while j >= 0 and k - j <= d and arr[j] < arr[k]:
                ans = max(ans, f(j) + 1)
                j -= 1
            j = k + 1
            while j < n and j - k <= d and arr[j] < arr[k]:
                ans = max(ans, f(j) + 1)
                j += 1
            dp[k] = ans
            return ans
                
        for i in range(n):
            f(i)
        return max(dp)

