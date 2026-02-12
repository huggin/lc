class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        cnt = [[0] * 26 for _ in range(n + 1)]
        ans = 0
        for i in range(n):
            for j in range(26):
                cnt[i + 1][j] = cnt[i][j]
            cnt[i + 1][ord(s[i]) - ord("a")] += 1

        def ok(i, j):
            ans = -1
            for k in range(26):
                d = cnt[i][k] - cnt[j][k]
                if d == 0:
                    continue
                elif ans == -1:
                    ans = d
                elif ans != d:
                    return False
            return True

        for i in range(n):
            for j in range(i, n):
                if ok(j + 1, i):
                    ans = max(ans, j - i + 1)
        return ans
