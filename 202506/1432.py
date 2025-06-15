class Solution:
    def maxDiff(self, num: int) -> int:
        s = list(int(c) for c in str(num))
        n = len(s)
        ma = s[:]
        mi = s[:]
        found = -1
        for i in range(n):
            if found != -1:
                if s[i] == found:
                    ma[i] = 9
            elif s[i] != 9:
                found = s[i]
                ma[i] = 9

        if mi[0] != 1:
            found = mi[0]
            mi[0] = 1
            for i in range(1, n):
                if mi[i] == found:
                    mi[i] = 1
        else:
            found = -1
            for i in range(1, n):
                if found != -1:
                    if s[i] == found:
                        mi[i] = 0
                elif s[i] != 0 and s[i] != 1:
                    found = s[i]
                    mi[i] = 0

        mi = int("".join(str(c) for c in mi))
        return int("".join(str(c) for c in ma)) - mi
