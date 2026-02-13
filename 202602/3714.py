class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        ans = 1
        curr = 1
        for i in range(1, n):
            if s[i] != s[i - 1]:
                ans = max(ans, curr)
                curr = 1
            else:
                curr += 1
        ans = max(ans, curr)

        def f(a):
            d = {0: -1}
            cnt = 0
            ans = 0
            for i in range(n):
                if s[i] not in a:
                    d = {0: i}
                    cnt = 0
                elif s[i] == a[0]:
                    cnt += 1
                else:
                    cnt -= 1
                if cnt in d:
                    ans = max(ans, i - d[cnt])
                else:
                    d[cnt] = i
            return ans

        for two in ["ab", "bc", "ac"]:
            ans = max(ans, f(two))

        d = {(0, 0): -1}
        cnt1, cnt2 = 0, 0
        for i in range(n):
            if s[i] == "a":
                cnt1 += 1
                cnt2 += 1
            elif s[i] == "b":
                cnt1 -= 1
            else:
                cnt2 -= 1
            if (cnt1, cnt2) in d:
                ans = max(ans, i - d[(cnt1, cnt2)])
            else:
                d[(cnt1, cnt2)] = i
        return ans
