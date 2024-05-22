class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1

        for i in range(1, n):
            if s[i - 1] == s[i]:
                dp[i - 1][i] = 1

        for k in range(2, n):
            for i in range(n):
                j = k + i
                if j >= n:
                    break
                if s[i] == s[j] and dp[i + 1][j - 1] == 1:
                    dp[i][j] = 1

        ans = []

        def solve(k, curr):
            if k == n:
                ans.append(curr[:])
                return

            for i in range(k, n):
                if dp[k][i] == 1:
                    curr.append(s[k : i + 1])
                    solve(i + 1, curr)
                    curr.pop()

        curr = []
        solve(0, curr)
        return ans
