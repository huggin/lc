class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        s = list(range(1, n + 2))
        for c in permutations(s):
            ok = True
            for i in range(1, len(c)):
                if (
                    c[i] - c[i - 1] > 0
                    and pattern[i - 1] == "D"
                    or c[i] - c[i - 1] < 0
                    and pattern[i - 1] == "I"
                ):
                    ok = False
                    break
            if ok:
                return "".join(str(i) for i in c)

        return ""
