class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        def f(i, j):
            if i > j:
                return ""
            cnt = 0
            a = []
            ii = i
            for k in range(i, j + 1):
                cnt += 1 if s[k] == "1" else -1
                if cnt == 0:
                    a.append((ii, k))
                    ii = k + 1
            if len(a) == 1:
                return "1" + f(i + 1, j - 1) + "0"

            a = [f(ii, jj) for (ii, jj) in a]
            a.sort(reverse=True)
            return "".join(a)

        return f(0, len(s) - 1)
