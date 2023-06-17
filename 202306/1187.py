class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()
        n = len(arr1)
        dp = [{} for _ in range(n)]
        dp[0][arr1[0]] = 0
        if arr2[0] < arr1[0]:
            dp[0][arr2[0]] = 1

        for i in range(1, n):
            for k, v in dp[i - 1].items():
                if k < arr1[i]:
                    if arr1[i] in dp[i]:
                        dp[i][arr1[i]] = min(dp[i][arr1[i]], v)
                    else:
                        dp[i][arr1[i]] = v

                idx = bisect.bisect(arr2, k)
                if idx == len(arr2):
                    continue
                if arr2[idx] in dp[i]:
                    dp[i][arr2[idx]] = min(dp[i][arr2[idx]], v + 1)
                else:
                    dp[i][arr2[idx]] = v + 1
        ans = n + 1
        for k, v in dp[n - 1].items():
            ans = min(ans, v)
        return ans if ans != n + 1 else -1
