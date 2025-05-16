class Solution:
    def getWordsInLongestSubsequence(
        self, words: List[str], groups: List[int]
    ) -> List[str]:
        n = len(words)
        dp = [1] * n
        pre = [-1] * n
        g = [[0] * n for _ in range(n)]

        def ok(i, j):
            if len(words[i]) != len(words[j]) or groups[i] == groups[j]:
                return False
            cnt = 0
            for k in range(len(words[i])):
                if words[i][k] != words[j][k]:
                    cnt += 1
            return cnt == 1

        for i in range(n):
            for j in range(i + 1, n):
                if ok(i, j):
                    g[i][j] = 1

        for i in range(n):
            for j in range(0, i):
                if g[j][i]:
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        pre[i] = j

        ma = 0
        pos = -1
        for i in range(n):
            if ma < dp[i]:
                pos = i
                ma = dp[i]

        ans = [pos]
        while pre[pos] != -1:
            pos = pre[pos]
            ans.append(pos)

        return [words[i] for i in reversed(ans)]
