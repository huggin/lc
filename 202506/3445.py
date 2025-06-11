class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        s = list(int(c) for c in s)
        ac = list(set(s))
        n = len(s)
        ans = -n

        def f(a, b):
            cnt = [[n] * 2 for _ in range(2)]
            cnt[0][0] = 0
            ca, cb = [0] * n, [0] * n
            ans = -n
            for i in range(k):
                if i > 0:
                    ca[i] = ca[i - 1]
                    cb[i] = cb[i - 1]
                if s[i] == a:
                    ca[i] += 1
                elif s[i] == b:
                    cb[i] += 1
            if ca[i] & 1 and cb[i] > 0 and (cb[i] & 1) == 0:
                ans = ca[i] - cb[i]

            j = 0
            for i in range(k, n):
                ca[i] = ca[i - 1]
                cb[i] = cb[i - 1]
                if s[i] == a:
                    ca[i] += 1
                elif s[i] == b:
                    cb[i] += 1
                while i - j + 1 > k and ca[i] - ca[j] > 0 and cb[i] - cb[j] > 0:
                    cnt[ca[j] & 1][cb[j] & 1] = min(
                        cnt[ca[j] & 1][cb[j] & 1], ca[j] - cb[j]
                    )
                    j += 1
                if ca[i] > 0 and cb[i] > 0:
                    ans = max(ans, ca[i] - cb[i] - cnt[1 - (ca[i] & 1)][cb[i] & 1])
            return ans

        for i in ac:
            for j in ac:
                if i == j:
                    continue
                ans = max(ans, f(i, j))
        return ans
