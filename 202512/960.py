class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs[0])
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                flag = True
                for k in range(len(strs)):
                    if strs[k][i] < strs[k][j]:
                        flag = False
                        break
                if flag:
                    dp[i] = max(dp[i], dp[j]+1)
        return n - max(dp)
