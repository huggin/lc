class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        def zf(s):
            n = len(s)
            z = [0] * n
            l, r = 0, 0
            for i in range(1, n):
                if i < r:
                    z[i] = min(r - i, z[i - l])
                while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                    z[i] += 1
                if i + z[i] > r:
                    l, r = i, i + z[i]
            z[0] = n
            return z

        n = len(lcp)
        for i in range(n):
            if lcp[i][i] != n - i:
                return ""
        for i in range(n):
            for j in range(n):
                if lcp[i][j] != lcp[j][i]:
                    return ""

        curr = 0
        idx = [-1] * n
        for i in range(n):
            if idx[i] == -1:
                idx[i] = curr
                curr += 1
            for j in range(i + 1, n):
                if lcp[i][j] > 0:
                    if j + lcp[i][j] > n:
                        return ""
                    if idx[j] == -1:
                        idx[j] = idx[i]
                    elif idx[j] != idx[i]:
                        return ""

        if curr > 26:
            return ""
        for i in range(n):
            z = zf(idx[i:])
            if z != lcp[i][i:]:
                return ""
        return "".join(chr(ord("a") + idx[i]) for i in range(n))
